---
name: italianizer
description: Scrive e riscrive testi in italiano naturale, eliminando lo slop AI-generated (lessico gonfiato, gerundi appesi, strutture meccaniche, calchi dall'inglese, attribuzioni vaghe). Pattern estratti da corpora italiani pre-AI in cinque registri (cronaca, saggistica, divulgazione, manualistica tecnica, giornalismo scientifico) più i segni di scrittura AI catalogati da Wikipedia. Legge sempre il testo per intero e riscrive preservando la coerenza narrativa. Usala quando l'utente chiede di scrivere/riscrivere/rivedere un testo in italiano, di "italianizzare" un testo, di togliere il sapore AI da un testo, o invoca /italianizer.
---

# Italianizer — italiano umano, senza slop AI

Applica i pattern di scrittura dell'italiano vero (pre-AI) a qualunque testo: nuovo o da riscrivere.
I pattern derivano da corpora reali in cinque registri diversi — cronaca e commento giornalistico,
saggistica, divulgazione pratica, manualistica tecnica, giornalismo scientifico — più il catalogo
dei segni di scrittura AI documentato da Wikipedia (WikiProject AI Cleanup), adattato all'italiano.
La skill è agnostica al contesto: sceglie il registro dal testo e dal destinatario, non impone
uno stile unico.

`SKILL=~/.claude/skills/italianizer` · reference in `$SKILL/references/`, script in `$SKILL/scripts/`.

## Quando usarla

- Scrivere un testo nuovo in italiano (articolo, email, post, documentazione, syllabus, landing copy)
- Riscrivere/ripulire un testo italiano che "sa di AI"
- Revisionare contenuto AI-generated prima della consegna
- L'utente invoca /italianizer o chiede esplicitamente detection/cleanup dello slop

## Workflow

### 0. Leggi tutto il testo, prima

Se il testo da rivedere esiste già, **leggilo integralmente prima di toccare una riga**
(con Read, per intero — non a campione). La riscrittura deve preservare il senso narrativo:

- **Arco**: il testo ha un inizio, uno sviluppo e una chiusura che si richiamano.
  Riscrivere un paragrafo ignorando dove il testo sta andando rompe l'arco.
- **Anafore e richiami**: "come detto sopra", un esempio introdotto prima e ripreso dopo,
  un termine definito al primo uso — se sposti o tagli, sistema i richiami.
- **Terminologia coerente**: scelto un termine per un concetto, resta quello in tutto il
  testo (la variatio forzata è slop, vedi reference).
- **Registro unico**: individua il registro dominante (e l'allocutivo) dal testo intero,
  poi applicalo ovunque. Non decidere il tono dal primo paragrafo.

Lavora sezione per sezione solo dopo la lettura integrale, tenendo conto di cosa precede
e cosa segue. A fine lavoro rileggi il risultato da cima a fondo: le giunture tra parti
riscritte e non riscritte sono il punto dove la coerenza si rompe.

### 1. Rileva

Per file di testo esistenti:

```bash
python3 $SKILL/scripts/detect_slop.py <file> [--verbose]
```

Restituisce uno slop score (0–100, più alto = peggio), i pattern trovati con riga e contesto,
e i check strutturali (densità di elenchi puntati, grassetti, connettivi meccanici, uniformità delle frasi).

Per la detection manuale o per scrivere da zero, leggi i reference:
- `references/slop-italiano.md` — pattern da eliminare, con correzioni
- `references/italiano-umano.md` — pattern positivi dai corpora, con esempi reali
- `references/microcopy-ui.md` — quarto registro: CTA, errori, testi di interfaccia,
  landing (auto-evidenza, brevitas, coerenza allocutiva tu/voi/lei, tono sociale)

### 2. Correggi

Riscrivi applicando i principi qui sotto. Non fare search-replace meccanico: lo slop è
strutturale prima che lessicale. Se togli "fondamentale" ma il periodo resta vuoto, hai
solo nascosto il problema.

## Principi (sintesi — dettagli e esempi nei reference)

**Concretezza.** Nomi propri, numeri, luoghi, orari, quantità al posto delle categorie astratte.
La cronaca vera non scrive "un episodio significativo in montagna": scrive "una slavina larga
30 metri e lunga 300" che travolge "il giovane... a una quota di 2.800 metri, fra le 11.30 e
le 11.40". Se non hai il dato, chiedilo o taci — non riempire con l'astratto.

**Ritmo variabile.** Frasi corte dopo periodi lunghi. Paragrafi disuguali. L'AI produce
paragrafi-fotocopia da 3 frasi l'uno; gli umani no.

**Presa di posizione.** Indicativo, giudizi netti, zero hedging. La saggistica vera commenta
le proprie fonti ("Una definizione asettica, ma che esplicita subito i diritti civili e
politici"); il commento giornalistico conclude ("la soluzione non può che essere pragmatica").

**Onestà sui limiti.** La scrittura umana dice cosa non funziona, con la stessa precisione
con cui promuove ("non si potrà giocare l'ultimo Tomb Raider in full HD su un computer di
20 anni fa"). Gli ostacoli si nominano uno per uno, dentro il discorso — mai in una
sezione-formula "Sfide e prospettive future".

**Prosa prima di tutto.** Elenchi puntati solo per enumerazioni vere (ingredienti, requisiti).
Le procedure si scrivono in prosa numerata fluida, come le ricette. Niente titoletti sotto
le 400 parole. Niente grassetto come evidenziatore compulsivo.

**Connettivi vivi.** "Per di più", "intanto", "frattanto", "eppure", "del resto", "peraltro",
"anzi" — non la triade meccanica Inoltre/Tuttavia/Infine a inizio paragrafo.

**Persone che fanno cose.** Soggetti animati e voce attiva. Fonti attribuite ("Come riferito
dalla Provincia autonoma"), persone con nome e cognome, discorso diretto con caporali «».

**Chiusure secche.** "Ecc." chiude un elenco aperto; una frase chiude un testo. Niente
"In conclusione, possiamo affermare che...", niente morale finale ottimista.

**Registro giusto, non elevato.** Ogni ambito ha il suo lessico proprio (il verricello,
il seracco, il bootloader, il tetto al contante): usalo. L'italiano genericamente "alto"
e vago è slop.

**Anima.** Il testo pulito ma senza voce è slop quanto quello gonfio: reagisci ai fatti
invece di elencarli, ammetti il dubbio e i giudizi misti ("semplici ma divertenti"),
concediti un inciso personale. Dettagli in `italiano-umano.md` §15.

## Anti-pattern rapidi (top 12 — lista completa nel reference)

1. ~~"In un mondo sempre più digitale..."~~ → parti dal fatto
2. ~~"svolge un ruolo cruciale/fondamentale"~~ → di' cosa fa, concretamente
3. ~~"Non solo X, ma anche Y" / "non è solo X: è Y"~~ → una cosa alla volta
4. ~~"È importante sottolineare che..."~~ → cancella, tieni solo il contenuto
5. ~~terne retoriche ("veloce, efficace e sicuro")~~ → uno o due aggettivi motivati
6. ~~"Andiamo a vedere / Scopriamo insieme"~~ → mostra e basta
7. ~~"vasta gamma", "molteplici", "una serie di"~~ → il numero vero o niente
8. ~~"impattare", "performante", "efficientare", "senza soluzione di continuità"~~ → verbi italiani
9. ~~"In conclusione / In sintesi" + riassunto~~ → chiudi sul punto più forte
10. ~~em-dash (—), bullet ovunque, grassetti ovunque~~ → incisi con trattino breve
    spaziato ("Quello che si osserva - e che è facilmente visibile - sono..."), prosa
11. ~~gerundio appeso ("...garantendo un'esperienza ottimale")~~ → frase propria col dato, o taglia
12. ~~"si pone come", "rappresenta un", "vanta"~~ → "è", "ha"

## Verifica finale

Rilancia `detect_slop.py` sul testo prodotto. Target: slop score < 20; GULPEASE > 60 per
microcopy/landing/divulgazione, > 40 per saggistica e testi tecnici. Lo script segnala
anche la mescolanza di allocutivi (tu/voi): sceglierne uno e tenerlo.

Poi la prova di pronuncia: quando leggiamo, il cervello lavora come se parlasse — se una
frase inciampa detta ad alta voce, inciampa anche letta. Se non la diresti a un collega,
riscrivila.
