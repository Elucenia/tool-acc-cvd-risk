# PCE2013 · modello storico

Riproduce l’equazione storica del 2013 per il primo infarto non fatale, morte coronarica o ictus fatale/non fatale in dieci anni. Non stima insufficienza cardiaca, rischio nell’arco della vita o effetti dei trattamenti.

## Metodo ed edizione

PCE2013 · coefficienti pubblicati nell’Appendice 4, Tabelle A/B; modello storico

## Dati in ingresso

- **Sesso nell’equazione pubblicata** (`sex`, `sel`)
  - `female`: Femminile
  - `male`: Maschile
- **Gruppo della popolazione di derivazione** (`population`, `sel`)
  - `nonHispanicWhite`: Persona bianca non ispanica
  - `nonHispanicAfricanAmerican`: Persona afroamericana non ispanica
  - `unsupported`: Altro gruppo / non determinato
- **Età** (`ageYears`, `num`) — anni [40–79]
- **Colesterolo totale** (`totalCholesterolMgDl`, `num`) — mg/dL [130–320]
- **Colesterolo HDL** (`hdlCholesterolMgDl`, `num`) — mg/dL [20–100]
- **Pressione arteriosa sistolica** (`systolicBpMmHg`, `num`) — mmHg [90–200]
- **Trattamento antipertensivo attuale?** (`treatedBp`, `sel`)
  - `yes`: Sì
  - `no`: No
- **Fumo attuale?** (`smoker`, `sel`)
  - `yes`: Sì
  - `no`: No
- **Diabete?** (`diabetes`, `sel`)
  - `yes`: Sì
  - `no`: No
- **Pregresso infarto miocardico?** (`priorMI`, `sel`)
  - `yes`: Sì
  - `no`: No
  - `unknown`: Sconosciuto
- **Pregresso ictus?** (`priorStroke`, `sel`)
  - `yes`: Sì
  - `no`: No
  - `unknown`: Sconosciuto
- **Pregressa insufficienza cardiaca?** (`priorHF`, `sel`)
  - `yes`: Sì
  - `no`: No
  - `unknown`: Sconosciuto
- **Pregresso intervento coronarico percutaneo?** (`priorPCI`, `sel`)
  - `yes`: Sì
  - `no`: No
  - `unknown`: Sconosciuto
- **Pregresso bypass coronarico?** (`priorCABG`, `sel`)
  - `yes`: Sì
  - `no`: No
  - `unknown`: Sconosciuto
- **Pregressa fibrillazione atriale?** (`atrialFibrillation`, `sel`)
  - `yes`: Sì
  - `no`: No
  - `unknown`: Sconosciuto
- **Condizione apparentemente sana alla valutazione basale confermata?** (`apparentlyHealthy`, `sel`)
  - `yes`: Sì
  - `no`: No
  - `unknown`: Sconosciuto
- **Uso del modello storico per ricerca confermato?** (`historicalResearchConfirmed`, `sel`)
  - `yes`: Sì
  - `no`: No
  - `unknown`: Sconosciuto

## Limiti e revisione

Le categorie della popolazione sono le due categorie storiche statunitensi della fonte; non sostituire altri gruppi implicitamente. Età: 40–79 anni; colesterolo totale: 130–320 mg/dL; HDL: 20–100 mg/dL; pressione sistolica: 90–200 mmHg. I tre limiti di laboratorio/pressione sono convenzioni del precedente stimatore ufficiale. Rispondere esplicitamente ad anamnesi e conferme; risposte sconosciute o esclusioni non producono stime. L’ACC dichiara che il rischio a dieci anni derivato da PCE non è più sostenuto dalle politiche cliniche/linee guida attuali. È un candidato di ricerca storica, non PREVENT, consiglio terapeutico o validazione clinica. Un esempio pubblicato per un uomo bianco resta discordante: l’equazione con coefficienti pubblicati arrotonda a 5,4%, mentre la tabella riporta 5,3%. Nessun coefficiente è stato modificato per nascondere la differenza. Permesso di distribuzione non ottenuto; revisione clinica/professionale non effettuata.

L’ACC dichiara che il rischio a dieci anni derivato da PCE non è più sostenuto dalle politiche cliniche/linee guida attuali. È un candidato di ricerca storica, non PREVENT, consiglio terapeutico o validazione clinica. Un esempio pubblicato per un uomo bianco resta discordante: l’equazione con coefficienti pubblicati arrotonda a 5,4%, mentre la tabella riporta 5,3%. Nessun coefficiente è stato modificato per nascondere la differenza. Permesso di distribuzione non ottenuto; revisione clinica/professionale non effettuata.

Le verifiche tecniche usano dati sintetici. Non sono state eseguite una revisione clinica indipendente e una revisione professionale delle traduzioni.

## Eseguire con dati sintetici

```sh
node cli.cjs examples/input.json it
```

## Risultati

- Stima storica a 10 anni (%)
<p>Probabilità a 10 anni = 1 − S₀<sup>exp(ΣβX − media)</sup>; percentuale = 100 × probabilità. X usa logaritmi naturali e interazioni della colonna popolazione/sesso pubblicata. Si conserva la precisione pubblicata dei coefficienti; la visualizzazione con un decimale non cambia il risultato grezzo.</p>

## Fonte e diritti

- https://doi.org/10.1161/01.cir.0000437741.48606.98
- https://www.heart.org/-/media/Data-Import/downloadables/0/D/A/2013-AHA-ACC-Cardiovascular-Risk-Guidelines-UCM_464291.pdf
- https://tools.acc.org/cvd-risk-estimator-plus/

[RIGHTS-SCOPE.md](../RIGHTS-SCOPE.md) · [test receipts](../evidence/)
