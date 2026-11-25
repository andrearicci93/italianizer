#!/usr/bin/env python3
"""Rileva pattern di slop AI in testi italiani.

Uso: detect_slop.py <file> [--verbose]

Output: slop score 0-100 (piu' alto = peggio), findings con riga e contesto,
check strutturali. Solo stdlib.
"""
import re
import statistics
import sys

# (regex, peso, etichetta) — case-insensitive salvo indicazione
LEXICAL_PATTERNS = [
    # Aperture vuote
    (r"in un mondo (sempre piu|in continua)", 8, "apertura vuota 'in un mondo...'"),
    (r"nell'era (digitale|dell'intelligenza|dei social|moderna)", 8, "apertura 'nell'era...'"),
    (r"viviamo in un'epoca", 8, "apertura 'viviamo in un'epoca'"),
    (r"quando si parla di", 3, "apertura 'quando si parla di'"),
    (r"in questo (articolo|post|testo|documento) (vedremo|esploreremo|analizzeremo|scopriremo)", 8, "meta-commento sul testo"),
    # Lessico gonfiato
    (r"\bcruciale\b", 4, "'cruciale'"),
    (r"\bfondamentale\b", 2, "'fondamentale'"),
    (r"\bimprescindibile\b", 4, "'imprescindibile'"),
    (r"(svolge|gioca|ricopre) un ruolo (chiave|cruciale|fondamentale|centrale)", 8, "'svolge un ruolo chiave'"),
    (r"\ball'avanguardia\b", 5, "'all'avanguardia'"),
    (r"\brivoluzionari[oa]\b", 4, "'rivoluzionario'"),
    (r"\bvibrante\b", 6, "'vibrante'"),
    (r"panorama (in continua evoluzione|in evoluzione)", 8, "'panorama in evoluzione'"),
    (r"in continua evoluzione", 6, "'in continua evoluzione'"),
    (r"\becosistema\b", 3, "'ecosistema' metaforico"),
    (r"una realta (innovativa|dinamica|consolidata|leader)", 7, "'una realta' per 'azienda'"),
    (r"\bpoliedric[oa]\b", 4, "'poliedrico'"),
    (r"\bolistic[oa]\b", 6, "'olistico'"),
    (r"\bsinergi[ac]", 5, "'sinergia/sinergico'"),
    (r"a 360 gradi", 7, "'a 360 gradi'"),
    (r"(una vasta|un'ampia) gamma", 6, "'vasta gamma'"),
    (r"un ampio ventaglio", 6, "'ampio ventaglio'"),
    (r"\bmolteplici\b", 3, "'molteplici'"),
    (r"un connubio", 5, "'un connubio'"),
    (r"fare la differenza", 5, "'fare la differenza'"),
    (r"plasmare il futuro", 8, "'plasmare il futuro'"),
    (r"un viaggio alla scoperta", 8, "'un viaggio alla scoperta'"),
    (r"\bimmergersi\b|\bimmergerti\b|\bimmergervi\b", 4, "'immergersi'"),
    (r"addentrarsi nei meandri", 8, "'addentrarsi nei meandri'"),
    (r"scoprire i segreti", 6, "'scoprire i segreti'"),
    (r"scopriamo insieme|vediamo insieme", 7, "'scopriamo/vediamo insieme'"),
    (r"andiamo a (vedere|scoprire|analizzare|capire)", 6, "'andiamo a + infinito'"),
    # Calchi dall'inglese
    (r"\bimpattante\b|\bimpattare\b|\bimpatta\b", 5, "'impattare'"),
    (r"\bperformante\b|\bperformare\b", 5, "'performante'"),
    (r"\befficientare\b", 6, "'efficientare'"),
    (r"\battenzionare\b|\battenzionat", 6, "'attenzionare'"),
    (r"senza soluzione di continuita", 6, "'senza soluzione di continuita' (seamless)"),
    (r"abbracciare (il cambiamento|l'innovazione|la trasformazione)", 7, "'abbracciare il cambiamento'"),
    (r"sposare (una filosofia|la causa|l'approccio)", 5, "'sposare una filosofia'"),
    (r"andare incontro alle esigenze", 5, "'andare incontro alle esigenze'"),
    (r"\bresilien(za|te)\b", 3, "'resilienza' fuori contesto tecnico"),
    # Strutture meccaniche
    (r"non solo [^.,;]{3,40}, ma (anche )?", 3, "'non solo... ma anche'"),
    (r"non e solo [^.,;:]{3,40}[:,] e ", 7, "'non e solo X: e Y'"),
    (r"che si tratti di", 5, "'che si tratti di X o Y'"),
    (r"\bin termini di\b", 3, "'in termini di'"),
    (r"\ba livello di\b", 3, "'a livello di'"),
    (r"\bal fine di\b", 3, "'al fine di'"),
    (r"\bnell'ottica di\b", 4, "'nell'ottica di'"),
    (r"risulta essere", 4, "'risulta essere'"),
    (r"si configura come", 5, "'si configura come'"),
    (r"andare a (costituire|definire|delineare|creare)", 5, "'andare a costituire'"),
    # Zavorra e hedging
    (r"e importante (sottolineare|notare|ricordare|evidenziare)", 7, "'e importante sottolineare'"),
    (r"vale la pena (notare|ricordare|sottolineare)", 6, "'vale la pena notare'"),
    (r"va (detto|sottolineato|ricordato|notato) che", 4, "'va detto che'"),
    (r"c'e da dire che", 4, "'c'e da dire che'"),
    (r"in (qualche modo|un certo senso)", 3, "hedging 'in qualche modo'"),
    (r"potrebbe potenzialmente", 7, "'potrebbe potenzialmente'"),
    (r"\btendenzialmente\b", 3, "'tendenzialmente'"),
    (r"\bestremamente\b", 3, "'estremamente'"),
    (r"\bincredibilmente\b", 4, "'incredibilmente'"),
    (r"\bassolutamente\b", 3, "'assolutamente'"),
    # Chiusure vuote
    (r"in conclusione", 5, "'in conclusione'"),
    (r"\bin sintesi\b", 4, "'in sintesi'"),
    (r"in (definitiva|ultima analisi)", 5, "'in definitiva'"),
    (r"il futuro e (gia )?(qui|adesso|ora)", 8, "'il futuro e gia qui'"),
    (r"le possibilita sono infinite", 8, "'le possibilita sono infinite'"),
    (r"non (ti |vi )?resta che", 5, "'non resta che'"),
    (r"e tu,? cosa ne pensi", 8, "'e tu cosa ne pensi?'"),
    # Sycophancy
    (r"ottima domanda", 8, "'ottima domanda'"),
    (r"spero che (questo )?(ti|vi) sia (stato )?utile", 8, "'spero ti sia utile'"),
    # Evitamento della copula
    (r"si pone come", 5, "'si pone come' (usa 'e'')"),
    (r"si erge a", 6, "'si erge a'"),
    (r"funge da", 3, "'funge da'"),
    (r"\bvanta (oltre|una|un|piu di|numeros)", 5, "'vanta' (usa 'ha')"),
    # Enfasi indebita su svolte ed eredita'
    (r"(rappresenta|segna) (una svolta|un punto di svolta|un momento (cruciale|storico|epocale))", 8, "'rappresenta una svolta'"),
    (r"gett\w+ le basi per", 5, "'gettare le basi per'"),
    (r"apre la strada a", 4, "'apre la strada a'"),
    (r"segno indelebile", 7, "'segno indelebile'"),
    (r"e una testimonianza di", 6, "'e una testimonianza di'"),
    (r"si inserisce in un (piu ampio|contesto|quadro)", 5, "'si inserisce in un piu ampio...'"),
    (r"un punto di riferimento per", 4, "'un punto di riferimento per'"),
    (r"consolidando (il|la|le|i) (proprio|propria|sua|suo)", 6, "'consolidando il proprio ruolo'"),
    # Attribuzioni vaghe
    (r"gli esperti (ritengono|concordano|sostengono|affermano)", 7, "'gli esperti ritengono' (chi?)"),
    (r"(molti|diversi|alcuni) osservatori", 6, "'molti osservatori' (chi?)"),
    (r"alcuni critici (sostengono|affermano|ritengono)", 6, "'alcuni critici' (chi?)"),
    (r"e ampiamente riconosciuto", 6, "'e ampiamente riconosciuto' (da chi?)"),
    (r"secondo (diversi|numerosi|alcuni) studi", 5, "'secondo diversi studi' (quali?)"),
    # Sezioni-formula sfide e prospettive
    (r"nonostante (le sfide|queste sfide|le difficolta)", 6, "'nonostante le sfide'"),
    (r"sfide e opportunita", 6, "'sfide e opportunita'"),
    (r"prospettive future", 5, "'prospettive future'"),
    (r"guardando al futuro", 6, "'guardando al futuro'"),
    # Disclaimer da chatbot
    (r"sulla base delle informazioni disponibili", 8, "disclaimer da chatbot"),
    (r"i dettagli (specifici )?(sono|risultano) (limitati|scarsi)", 8, "disclaimer da chatbot"),
    (r"e (sempre )?consigliabile consultare", 6, "'e consigliabile consultare'"),
]

# Gerundi appesi: ", <gerundio slop>" in coda di frase — analisi finta
GERUNDI_SLOP = r", (garantendo|evidenziando|sottolineando|contribuendo|dimostrando|permettendo|consentendo|favorendo|promuovendo|rafforzando|offrendo cosi|creando cosi)\b"

CONNETTIVI_MECCANICI = r"^(inoltre|tuttavia|infine|in aggiunta|d'altra parte|dall'altro lato)\b"


def strip_accents(s: str) -> str:
    table = str.maketrans("àèéìòùÀÈÉÌÒÙ", "aeeiouAEEIOU")
    return s.translate(table)


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    verbose = "--verbose" in sys.argv
    if not args:
        print(__doc__)
        sys.exit(1)

    raw = open(args[0], encoding="utf-8", errors="replace").read()
    lines = raw.splitlines()
    text_norm = strip_accents(raw).lower()
    lines_norm = text_norm.splitlines()
    words = len(re.findall(r"\w+", raw))
    if words == 0:
        print("File vuoto.")
        sys.exit(0)

    findings = []  # (line_no, label, weight, context)
    penalty = 0.0
    for pattern, weight, label in LEXICAL_PATTERNS:
        for i, ln in enumerate(lines_norm):
            for m in re.finditer(pattern, ln):
                ctx = lines[i].strip()[:90]
                findings.append((i + 1, label, weight, ctx))
                penalty += weight

    # --- Check strutturali ---
    struct_notes = []

    # Gerundi appesi: soglia in densita' (il gerundio legittimo esiste in italiano)
    ger = len(re.findall(GERUNDI_SLOP, text_norm))
    if ger / (words / 1000) > 1.5:
        pen = min(12, ger * 3)
        penalty += pen
        struct_notes.append(f"{ger} gerundi appesi (', garantendo/evidenziando/...'): analisi finta in coda (+{pen})")

    # Liste con header in grassetto ("- **Titolo:** testo")
    bold_headers = sum(1 for ln in lines if re.match(r"\s*[-*•]\s+\*\*[^*]+:?\*\*", ln))
    if bold_headers >= 3:
        penalty += 8
        struct_notes.append(f"{bold_headers} voci di lista con header in grassetto: formato-vetrina AI (+8)")

    # Paragrafi che iniziano con connettivi meccanici
    paras = [p.strip() for p in re.split(r"\n\s*\n", text_norm) if p.strip()]
    mech = sum(1 for p in paras if re.match(CONNETTIVI_MECCANICI, p))
    if paras and mech / len(paras) > 0.15:
        pen = min(12, mech * 4)
        penalty += pen
        struct_notes.append(f"{mech}/{len(paras)} paragrafi aprono con Inoltre/Tuttavia/Infine (+{pen})")

    # Densita' di elenchi puntati
    bullets = sum(1 for ln in lines if re.match(r"\s*[-*•]\s+\S", ln))
    content_lines = sum(1 for ln in lines if ln.strip())
    if content_lines and bullets / content_lines > 0.35:
        penalty += 10
        struct_notes.append(f"{bullets}/{content_lines} righe sono bullet: troppa lista, poca prosa (+10)")

    # Em-dash: mai — gli incisi si fanno col trattino breve spaziato " - "
    emdash = raw.count("—") + len(re.findall(r"\s--\s", raw))
    if emdash > 0:
        per_kw = emdash / (words / 1000)
        pen = 8 if per_kw > 4 else 3
        penalty += pen
        struct_notes.append(f"{emdash} em-dash: sostituire con trattino breve spaziato ' - ' (+{pen})")

    # Grassetti
    bolds = len(re.findall(r"\*\*[^*]+\*\*", raw))
    if bolds / (words / 1000) > 12:
        penalty += 6
        struct_notes.append(f"{bolds} grassetti: evidenziatore compulsivo (+6)")

    # Uniformita' lunghezza frasi (ritmo piatto)
    sentences = [s for s in re.split(r"[.!?]+\s", re.sub(r"\s+", " ", raw)) if len(s.split()) >= 3]
    if len(sentences) >= 8:
        lens = [len(s.split()) for s in sentences]
        cv = statistics.pstdev(lens) / statistics.mean(lens)
        if cv < 0.35:
            penalty += 10
            struct_notes.append(f"frasi troppo uniformi (cv={cv:.2f}, media {statistics.mean(lens):.0f} parole): ritmo piatto (+10)")

    # Terne retoriche "X, Y e Z" con aggettivi
    triads = len(re.findall(r"\w+[oaie], \w+[oaie] e \w+[oaie]\b", text_norm))
    if triads / (words / 1000) > 5:
        penalty += 6
        struct_notes.append(f"{triads} possibili terne retoriche 'X, Y e Z' (+6)")

    # Coerenza allocutiva: mescolanza tu/voi rivolti al lettore
    tu_forms = len(re.findall(r"\b(puoi|vuoi|devi|sai|clicca|inserisci|scopri|iscriviti|il tuo|la tua|i tuoi|le tue)\b|\bti (?=\w)", text_norm))
    voi_forms = len(re.findall(r"\b(potete|volete|dovete|sapete|cliccate|inserite|scoprite|iscrivetevi|il vostro|la vostra|i vostri|le vostre)\b|\bvi (?!e\b|sono\b|era(no)?\b|fu\b|fosse(ro)?\b|sia(no)?\b)(?=\w)", text_norm))
    # Solo se la forma minoritaria e' davvero frequente (>=1 ogni 1000 parole):
    # nelle raccolte lunghe multi-articolo la mescolanza tra pezzi diversi e' legittima.
    if tu_forms >= 2 and voi_forms >= 2 and min(tu_forms, voi_forms) / (words / 1000) >= 1.0:
        penalty += 8
        struct_notes.append(f"allocutivi mescolati: {tu_forms} forme col tu, {voi_forms} col voi — sceglierne uno (+8)")

    # GULPEASE: indice di leggibilita' per l'italiano (0-100, alto = leggibile)
    letters = len(re.findall(r"[a-zA-Zàèéìòù]", raw))
    n_sent = max(1, len(re.findall(r"[.!?]+", raw)))
    gulpease = max(0, min(100, 89 + (300 * n_sent - 10 * letters) / words))
    if gulpease > 80:
        g_note = "molto facile"
    elif gulpease > 60:
        g_note = "facile (ok per microcopy/landing/divulgazione)"
    elif gulpease > 40:
        g_note = "medio (ok per saggistica/testi tecnici)"
    else:
        g_note = "difficile: frasi o parole troppo lunghe"

    # Score normalizzato sulla lunghezza (penalita' per 1000 parole, cap 100)
    score = min(100, round(penalty / (words / 1000) * 1.5))

    print(f"File: {args[0]}  ({words} parole)")
    print(f"SLOP SCORE: {score}/100  " + ("— pulito" if score < 20 else "— da rivedere" if score < 45 else "— slop pesante"))
    print(f"GULPEASE: {gulpease:.0f}/100 — {g_note}")
    print()
    if findings:
        print(f"Pattern lessicali trovati: {len(findings)}")
        shown = findings if verbose else findings[:20]
        for line_no, label, weight, ctx in shown:
            print(f"  r.{line_no:>4}  [{weight}] {label}\n         {ctx}")
        if not verbose and len(findings) > 20:
            print(f"  ... e altri {len(findings) - 20} (usa --verbose)")
    else:
        print("Nessun pattern lessicale trovato.")
    if struct_notes:
        print("\nCheck strutturali:")
        for n in struct_notes:
            print(f"  - {n}")


if __name__ == "__main__":
    main()
