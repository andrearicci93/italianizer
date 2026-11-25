# italianizer

Una skill per Claude Code che scrive e riscrive testi in italiano senza il sapore dell'AI: via le aperture vuote, il lessico gonfiato, i gerundi appesi, i «non solo X, ma anche Y», gli elenchi puntati messi ovunque.

I pattern vengono da corpora italiani scritti prima dell'AI generativa, in cinque registri (cronaca, saggistica, divulgazione pratica, manualistica tecnica, giornalismo scientifico), più il catalogo dei segni di scrittura AI di Wikipedia (WikiProject AI Cleanup), adattato all'italiano.

## Cosa c'è dentro

- `SKILL.md`: il workflow e i principi. Legge sempre il testo per intero prima di toccarlo.
- `references/slop-italiano.md`: i tic da eliminare, con la correzione accanto.
- `references/italiano-umano.md`: i pattern positivi, con esempi reali.
- `references/microcopy-ui.md`: bottoni, errori, landing, e la coerenza tra tu, voi e lei.
- `scripts/detect_slop.py`: dà un punteggio da 0 a 100 (più alto, peggio), mostra i pattern trovati con riga e contesto, calcola l'indice GULPEASE. Solo libreria standard, Python 3.

## Installazione

```bash
git clone https://github.com/andrearicci93/italianizer ~/.claude/skills/italianizer
```

Poi in Claude Code scrivi `/italianizer` seguito dal testo, oppure chiedi di «togliere il sapore AI» a un file.

Il detector funziona anche da solo:

```bash
python3 ~/.claude/skills/italianizer/scripts/detect_slop.py testo.md --verbose
```
