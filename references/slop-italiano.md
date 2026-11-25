# Slop italiano — pattern da eliminare

Catalogo dei tic dell'italiano AI-generated, con correzioni. Ordinati per priorità.
Integra, adattati all'italiano, i pattern documentati da Wikipedia ("Signs of AI writing",
WikiProject AI Cleanup).

## 1. Aperture vuote (cancellare sempre)

| Slop | Correzione |
|---|---|
| "In un mondo sempre più [digitale/connesso/veloce]..." | Parti dal fatto o dal soggetto |
| "Nell'era [digitale / dell'AI / dei social]..." | Idem |
| "Viviamo in un'epoca in cui..." | Idem |
| "Negli ultimi anni, X ha assunto un'importanza crescente" | Di' cosa è successo e quando |
| "Quando si parla di X, ..." | Parla di X e basta |
| "In questo articolo vedremo / esploreremo..." | Cancella il meta-commento, inizia |

## 2. Lessico gonfiato (sostituire con il concreto)

| Slop | Correzione |
|---|---|
| cruciale, fondamentale, essenziale, imprescindibile (a raffica) | motivare o togliere; al massimo uno per testo |
| "svolge/gioca/ricopre un ruolo chiave" | di' cosa fa: "gestisce", "decide", "paga" |
| innovativo, rivoluzionario, all'avanguardia, dinamico, vibrante | il dato che lo dimostra, o niente |
| "un panorama in continua evoluzione" | cosa è cambiato, quando |
| ecosistema, scenario, panorama (metaforici) | il nome vero della cosa: mercato, settore, città |
| "una realtà innovativa" (per: azienda) | "un'azienda", col nome |
| sfaccettato, poliedrico, olistico, sinergico | descrivere le facce, una per una |
| "a 360 gradi" | togliere |
| "vasta gamma", "ampio ventaglio", "una serie di", "molteplici" | il numero vero ("sei corsi", "tre casi") o niente |
| "un mix di", "un connubio tra", "un binomio" | nominare i due elementi e il rapporto |
| "fare la differenza" | quale differenza, misurata come |
| "plasmare il futuro" | togliere |
| "un viaggio alla scoperta di" | togliere |
| "immergersi in", "addentrarsi nei meandri di" | "leggere", "studiare", "usare" |
| "scoprire i segreti di" | "imparare", "capire" |

## 3. Calchi dall'inglese

| Slop | Correzione |
|---|---|
| impattare, impattante | incidere su, pesare su; "che incide" |
| performante, performare | veloce/efficiente; rendere, funzionare |
| efficientare | rendere più efficiente, snellire |
| attenzionare | segnalare, tenere d'occhio |
| processare (una richiesta) | elaborare, gestire, evadere |
| implementare (fuori dal codice) | attuare, realizzare, introdurre |
| "senza soluzione di continuità" (per seamless) | "senza interruzioni", o riscrivere |
| "abbracciare il cambiamento" | accettare, adottare — o dire cosa si fa |
| "sposare una filosofia" | seguire, condividere |
| supportare (per: sostenere) | sostenere, aiutare, reggere |
| "andare incontro alle esigenze" | rispondere a, servire |
| "prendere in carico" ovunque | occuparsi di, gestire |
| resilienza/resiliente (fuori contesto tecnico) | tenuta, capacità di ripresa |

## 4. Strutture meccaniche

**"Non solo X, ma anche Y" / "non è solo X: è Y"** — il tic più riconoscibile. Una cosa
alla volta: se Y è il punto, di' Y.

**Terna retorica** ("semplice, veloce e sicuro"; "analizzare, comprendere e agire") — l'AI
chiude ogni concetto con tre elementi. Uno o due, motivati, valgono di più.

**"Che si tratti di X o di Y"** — falso universale. Scegli il caso che interessa al lettore.

**"Dalla A alla B"** ("dalla progettazione al deployment") — falso range. Nomina le fasi
che contano.

**Frasi nominali a effetto** ("Semplice. Veloce. Sicuro.") — copywriting da template.

**"Andiamo a vedere / analizzare"** — l'andare a + infinito da telecronaca. "Vediamo" o,
meglio, mostra direttamente.

**"Vediamo insieme / Scopriamo insieme"** — falso noi inclusivo. Cancella.

**Paragrafi fotocopia** — tutti da 3 frasi, tutti aperti da un connettivo (Inoltre...,
Tuttavia..., Infine...). Vedi `italiano-umano.md` per il ritmo vero.

**Due punti + elenco puntato come struttura di default** — la prosa argomenta, l'elenco
enumera. Se gli elementi non sono davvero enumerabili (ingredienti, requisiti, passi),
scrivi in prosa.

**Domanda retorica + risposta immediata** ("Cosa significa questo? Significa che...") —
il testo si interroga da solo per darsi ragione. Le domande vere restano aperte qualche
riga (vedi corpus saggistica).

## 4-bis. Gerundio appeso (analisi finta in coda)

Il tic più tipico dell'AI in italiano: la frase finisce con un gerundio che aggiunge
profondità apparente — traduzione diretta delle "-ing endings" inglesi.

> "Il progetto integra dati da più fonti, **garantendo** una visione completa e
> **contribuendo** a migliorare l'esperienza utente."

Gerundi sorvegliati: *garantendo, evidenziando, sottolineando, contribuendo a,
dimostrando, permettendo, consentendo, favorendo, promuovendo, rendendo, offrendo,
creando così, rafforzando*.

**Correzione**: o l'informazione del gerundio merita una frase propria (con soggetto e
dato), o è aria e si taglia. "Il progetto incrocia i dati di X e Y. Nei test il tempo
di ricerca è sceso del 30%."

## 4-ter. Evitamento della copula

L'AI evita "è"/"sono"/"ha" con costruzioni pompose:

| Slop | Correzione |
|---|---|
| "si pone come", "si configura come", "si erge a" | "è" |
| "rappresenta un/una" (per: è) | "è" |
| "costituisce un/una" (per: è) | "è" |
| "funge da" | "è", "fa da" |
| "vanta [oltre X / una lunga tradizione]" | "ha" |
| "offre/presenta una vasta gamma di" | "ha", con il numero vero |

## 4-quater. Enfasi indebita su svolte ed eredità

L'AI gonfia l'importanza di qualunque cosa collegandola a trend più ampi:

| Slop | Correzione |
|---|---|
| "rappresenta/segna una svolta (epocale)" | cosa è cambiato, per chi, da quando |
| "un punto di svolta / un momento cruciale" | idem |
| "getta le basi per", "apre la strada a" | cosa succede dopo, se lo sai; altrimenti taglia |
| "lascia un segno indelebile" | taglia |
| "è una testimonianza di" | di' il fatto |
| "si inserisce in un più ampio contesto/movimento di" | taglia, o nomina il contesto con date e fatti |
| "un punto di riferimento per" | per chi, misurato come |
| "consolidando il proprio ruolo di" | taglia |

## 4-quinquies. Attribuzioni vaghe

| Slop | Correzione |
|---|---|
| "gli esperti ritengono/concordano" | chi? nome, ente, anno — o è opinione tua |
| "molti osservatori notano" | idem |
| "alcuni critici sostengono" | idem |
| "è ampiamente riconosciuto che" | idem |
| "secondo diversi studi" (senza citarli) | lo studio, l'anno, il dato |
| "si dice che", "è noto che" | fonte o niente |

## 4-sexies. Sezioni-formula "Sfide e prospettive"

Le chiusure da articolo AI: "Nonostante le sfide...", "Sfide e opportunità",
"Prospettive future", "Guardando al futuro...". Struttura fissa: elogio → sfide
generiche → ottimismo finale. **Correzione**: i problemi si nominano uno per uno, con
dati ("Uno è il costo. Un altro ostacolo è..."), dentro il discorso, non in una sezione
di servizio.

## 4-septies. Variatio forzata (giro di sinonimi)

L'AI evita di ripetere la stessa parola e cicla i sinonimi: "il protagonista... il
personaggio principale... la figura centrale... l'eroe". In italiano si aggiunge il
vizio giornalistico di terza mano ("il velivolo", "il quadrupede", "la kermesse").
**Correzione**: ripetere la parola giusta è lecito; il pronome esiste; i sinonimi si
usano quando aggiungono precisione, non per paura della ripetizione.

## 4-octies. Disclaimer da chatbot rimasti nel testo

- "Sulla base delle informazioni disponibili..."
- "Sebbene i dettagli specifici siano limitati..."
- "Al momento della stesura di questo testo..." (se non è davvero rilevante)
- "È sempre consigliabile consultare un professionista"

Sono residui di conversazione con l'AI, non contenuto. Via.

## 5. Zavorra e hedging

| Slop | Correzione |
|---|---|
| "È importante sottolineare/notare che..." | cancellare, tenere il contenuto |
| "Vale la pena ricordare che..." | idem |
| "Va detto che...", "C'è da dire che..." | idem |
| "in qualche modo", "in un certo senso" | prendere posizione o tacere |
| "potrebbe potenzialmente" | "può", o il condizionale secco |
| "tendenzialmente", "generalmente parlando" | quando sì e quando no |
| davvero, estremamente, incredibilmente, assolutamente | quasi sempre da togliere |
| "al fine di" | "per" |
| "in termini di" | riscrivere il complemento |
| "a livello di" | idem |
| "andare a costituire/definire" | "costituire", "definire" |
| "risulta essere" | "è" |
| "si configura come" | "è" |
| "nell'ottica di" | "per" |
| "in relazione a", "relativamente a" | "su", "per", "riguardo a" |

## 6. Chiusure vuote

- "In conclusione, possiamo affermare che..." + riassunto di quanto già detto → chiudi sul
  punto più forte, o su un fatto nuovo.
- "In sintesi / In definitiva / In ultima analisi" → idem.
- Morale ottimista finale ("Il futuro è già qui", "le possibilità sono infinite",
  "non resta che provare") → cancellare.
- "E tu, cosa ne pensi?" → cancellare.

## 7. Tipografia e formato

- **Em-dash (—): mai.** Per gli incisi l'italiano usa il trattino breve con spazi " - ":
  "Quello che si osserva - e che è facilmente visibile - sono i fenomeni...". È la
  convenzione dei corpora ("che - nel bene o nel male - modellano la stessa società").
  E comunque gli incisi col trattino solo *quando aggiungono informazione*, non come
  pausa drammatica seriale: l'alternativa sono virgole e parentesi.
- **Grassetti ovunque** — il grassetto evidenzia un termine la prima volta o un dato chiave.
  Non una frase per paragrafo.
- **Titoletti ogni 3 righe** — sotto le 400 parole non servono sezioni.
- **Liste con header in grassetto** ("- **Esperienza utente:** l'esperienza utente è
  stata migliorata...") — il formato-vetrina dell'AI. Riscrivere in prosa, o in elenco
  semplice se davvero enumerabile.
- **Title Case Nei Titoli** ("Le Sfide E Le Opportunità Del Digitale") — convenzione
  inglese, in italiano è sempre un errore: solo la prima parola maiuscola.
- **Emoji nei testi professionali** — no, salvo richiesta esplicita.
- **Virgolette**: l'italiano editoriale usa i caporali «» per il discorso diretto; gli
  apici doppi per citazioni brevi o distanziamento. Coerenza nel testo.

## 8. Sycophancy e servilismo (nelle risposte dirette)

- "Ottima domanda!", "Certamente!", "Assolutamente sì!" → rispondere e basta.
- "Spero che questo ti sia utile" → cancellare.
- Ripetere la domanda dell'utente riformulata prima di rispondere → cancellare.
