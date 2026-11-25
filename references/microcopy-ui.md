# Microcopy e testi di interfaccia

I testi di interfaccia (CTA, messaggi di errore, empty state, form, onboarding, landing)
sono un registro a parte, con regole proprie che i corpora editoriali non coprono.

## Auto-evidenza ("non costringermi a pensare")

Il testo di interfaccia si capisce senza sforzo o ha fallito. Non conta il numero di
passaggi: conta che ogni scelta sia priva di ambiguità.

- Bottoni con il verbo dell'azione, non l'etichetta astratta: "Scarica il programma",
  non "Download" o "Procedi".
- L'errore dice cosa è andato storto E cosa fare: "L'email non ha la @. Controllala
  e riprova", non "Errore di validazione".
- Se un microtesto richiede di essere riletto, riscrivilo.

## Brevitas

Regola classica dello UX writing:

> "Liberatevi della metà delle parole in ogni pagina, e poi della metà di quelle che
> rimangono."

Passata di taglio in due giri, sempre. Il microcopy tiene solo l'informazione minima
necessaria, nel punto esatto dove serve (tempestivo), formattato in modo che sia
impossibile non vederlo (inevitabile).

## Prova di pronuncia

Quando leggiamo, le aree senso-motorie del cervello lavorano come se stessimo parlando.
Se una frase è difficile da pronunciare, è difficile anche da leggere. Ogni microtesto
va detto ad alta voce: se inciampa la lingua, inciampa il lettore.

## Registro sociale, non commerciale

Le persone rispondono meglio alle regole sociali che a quelle di mercato: il tono
efficace è domestico-caldo, non commerciale-freddo. Un chatbot che scrive "La preghiamo
di voler cortesemente attendere" stona col mezzo; "Un attimo, ci siamo quasi" no.

Attenzione all'eccesso opposto: la finta amicizia da brand ("Ehi! Ci sei mancato! 🎉")
è slop quanto il burocratese. Il calore vero è concreto e utile, non esclamativo.

## Coerenza allocutiva (tu / voi / lei)

Errore tipico dei testi AI e dei siti tradotti: mescolare gli allocutivi nello stesso
flusso ("Inserisci la tua email" ... "Vi contatteremo al più presto" ... "La informiamo
che...").

- Scegliere **un** allocutivo per prodotto/brand e tenerlo ovunque: UI, email, errori.
- Default per prodotti digitali italiani: il **tu**.
- Il **lei** solo se il brand lo richiede davvero (banche, PA) — e allora ovunque.
- Il **voi** solo se ci si rivolge a un gruppo reale (una community, una classe: "postate
  le vostre foto"), non come via di mezzo timida.

`detect_slop.py` segnala la mescolanza tu/voi come check strutturale.

## Personas e voce

Prima di scrivere i microtesti di un prodotto, dare un carattere alla voce (chi parla?
com'è? cosa non direbbe mai?). Le persone riconoscono subito la voce dietro il testo
e si accorgono delle incongruenze: un tono giocoso nell'onboarding e notarile negli
errori tradisce che nessuno abita davvero quella voce.

## Verifica

- GULPEASE (in `detect_slop.py`): per microcopy e landing puntare **> 60** (facile per
  chi ha la licenza media). La saggistica può stare più bassa; un bottone no.
- Prova di parafrasi: chiedi (o chiediti) "cosa succede se clicco qui?" — se la
  risposta non è immediata e univoca, riscrivi.
