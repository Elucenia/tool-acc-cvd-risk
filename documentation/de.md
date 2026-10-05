# PCE2013 · historisches Modell

Reproduziert die historische Gleichung von 2013 für einen ersten nicht tödlichen Myokardinfarkt, Koronartod oder tödlichen/nicht tödlichen Schlaganfall innerhalb von zehn Jahren. Schätzt weder Herzinsuffizienz noch Lebenszeitrisiko oder Behandlungseffekte.

## Methode und Fassung

PCE2013 · veröffentlichte Koeffizienten in Anhang 4, Tabellen A/B; historisches Modell

## Eingaben

- **Geschlecht in der veröffentlichten Gleichung** (`sex`, `sel`)
  - `female`: Weiblich
  - `male`: Männlich
- **Gruppe der Ableitungspopulation** (`population`, `sel`)
  - `nonHispanicWhite`: Nicht hispanische weiße Person
  - `nonHispanicAfricanAmerican`: Nicht hispanische afroamerikanische Person
  - `unsupported`: Andere Gruppe / nicht bestimmt
- **Alter** (`ageYears`, `num`) — Jahre [40–79]
- **Gesamtcholesterin** (`totalCholesterolMgDl`, `num`) — mg/dL [130–320]
- **HDL-Cholesterin** (`hdlCholesterolMgDl`, `num`) — mg/dL [20–100]
- **Systolischer Blutdruck** (`systolicBpMmHg`, `num`) — mmHg [90–200]
- **Aktuelle antihypertensive Behandlung?** (`treatedBp`, `sel`)
  - `yes`: Ja
  - `no`: Nein
- **Aktuelles Rauchen?** (`smoker`, `sel`)
  - `yes`: Ja
  - `no`: Nein
- **Diabetes?** (`diabetes`, `sel`)
  - `yes`: Ja
  - `no`: Nein
- **Früherer Myokardinfarkt?** (`priorMI`, `sel`)
  - `yes`: Ja
  - `no`: Nein
  - `unknown`: Unbekannt
- **Früherer Schlaganfall?** (`priorStroke`, `sel`)
  - `yes`: Ja
  - `no`: Nein
  - `unknown`: Unbekannt
- **Frühere Herzinsuffizienz?** (`priorHF`, `sel`)
  - `yes`: Ja
  - `no`: Nein
  - `unknown`: Unbekannt
- **Frühere perkutane Koronarintervention?** (`priorPCI`, `sel`)
  - `yes`: Ja
  - `no`: Nein
  - `unknown`: Unbekannt
- **Frühere koronare Bypassoperation?** (`priorCABG`, `sel`)
  - `yes`: Ja
  - `no`: Nein
  - `unknown`: Unbekannt
- **Früheres Vorhofflimmern?** (`atrialFibrillation`, `sel`)
  - `yes`: Ja
  - `no`: Nein
  - `unknown`: Unbekannt
- **Anscheinend gesunder Zustand bei der Ausgangsuntersuchung bestätigt?** (`apparentlyHealthy`, `sel`)
  - `yes`: Ja
  - `no`: Nein
  - `unknown`: Unbekannt
- **Verwendung des historischen Modells für Forschung bestätigt?** (`historicalResearchConfirmed`, `sel`)
  - `yes`: Ja
  - `no`: Nein
  - `unknown`: Unbekannt

## Grenzen und Prüfung

Die Bevölkerungsgruppen sind die zwei historischen US-Kategorien der Quelle; andere Gruppen nicht stillschweigend ersetzen. Alter: 40–79 Jahre; Gesamtcholesterin: 130–320 mg/dL; HDL: 20–100 mg/dL; systolischer Druck: 90–200 mmHg. Die drei Labor-/Druckgrenzen sind Konventionen des früheren offiziellen Schätzers. Anamnese und Bestätigungen ausdrücklich beantworten; unbekannte Antworten oder Ausschlüsse ergeben keine Schätzung. Laut ACC wird das mit PCE berechnete Zehnjahresrisiko nicht mehr durch aktuelle klinische Richtlinien unterstützt. Dies ist ein historischer Forschungskandidat, nicht PREVENT, Therapieempfehlung oder klinische Validierung. Ein veröffentlichtes Beispiel für einen weißen Mann bleibt abweichend: Mit veröffentlichten Koeffizienten rundet die Gleichung auf 5,4 %, die Tabelle nennt 5,3 %. Koeffizienten wurden nicht zur Verdeckung der Abweichung geändert. Verbreitungsgenehmigung und klinische/professionelle Prüfung sind nicht erfolgt.

Laut ACC wird das mit PCE berechnete Zehnjahresrisiko nicht mehr durch aktuelle klinische Richtlinien unterstützt. Dies ist ein historischer Forschungskandidat, nicht PREVENT, Therapieempfehlung oder klinische Validierung. Ein veröffentlichtes Beispiel für einen weißen Mann bleibt abweichend: Mit veröffentlichten Koeffizienten rundet die Gleichung auf 5,4 %, die Tabelle nennt 5,3 %. Koeffizienten wurden nicht zur Verdeckung der Abweichung geändert. Verbreitungsgenehmigung und klinische/professionelle Prüfung sind nicht erfolgt.

Die technischen Prüfungen verwenden synthetische Daten. Eine unabhängige klinische Prüfung und eine professionelle Übersetzungsprüfung wurden nicht durchgeführt.

## Mit synthetischen Daten ausführen

```sh
node cli.cjs examples/input.json de
```

## Ergebnisse

- Historische 10-Jahres-Schätzung (%)
<p>10-Jahres-Wahrscheinlichkeit = 1 − S₀<sup>exp(ΣβX − Mittelwert)</sup>; Prozentwert = 100 × Wahrscheinlichkeit. X verwendet natürliche Logarithmen und Interaktionen der veröffentlichten Bevölkerungs-/Geschlechtsspalte. Die veröffentlichte Koeffizientenpräzision bleibt erhalten; eine Dezimalstelle in der Anzeige verändert das Rohergebnis nicht.</p>

## Quelle und Rechte

- https://doi.org/10.1161/01.cir.0000437741.48606.98
- https://www.heart.org/-/media/Data-Import/downloadables/0/D/A/2013-AHA-ACC-Cardiovascular-Risk-Guidelines-UCM_464291.pdf
- https://tools.acc.org/cvd-risk-estimator-plus/

[RIGHTS-SCOPE.md](../RIGHTS-SCOPE.md) · [test receipts](../evidence/)
