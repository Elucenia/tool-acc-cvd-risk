# PCE2013 · modelo histórico

Reproduce la ecuación histórica de 2013 para el primer infarto no mortal, muerte coronaria o ictus mortal/no mortal en diez años. No estima insuficiencia cardíaca, riesgo de por vida ni efectos del tratamiento.

## Método y edición

PCE2013 · coeficientes publicados en el Apéndice 4, Tablas A/B; modelo histórico

## Entradas

- **Sexo en la ecuación publicada** (`sex`, `sel`)
  - `female`: Femenino
  - `male`: Masculino
- **Grupo de población de derivación** (`population`, `sel`)
  - `nonHispanicWhite`: Persona blanca no hispana
  - `nonHispanicAfricanAmerican`: Persona afroamericana no hispana
  - `unsupported`: Otro grupo / no determinado
- **Edad** (`ageYears`, `num`) — años [40–79]
- **Colesterol total** (`totalCholesterolMgDl`, `num`) — mg/dL [130–320]
- **Colesterol HDL** (`hdlCholesterolMgDl`, `num`) — mg/dL [20–100]
- **Presión arterial sistólica** (`systolicBpMmHg`, `num`) — mmHg [90–200]
- **¿Tratamiento antihipertensivo actual?** (`treatedBp`, `sel`)
  - `yes`: Sí
  - `no`: No
- **¿Tabaquismo actual?** (`smoker`, `sel`)
  - `yes`: Sí
  - `no`: No
- **¿Diabetes?** (`diabetes`, `sel`)
  - `yes`: Sí
  - `no`: No
- **¿Infarto de miocardio previo?** (`priorMI`, `sel`)
  - `yes`: Sí
  - `no`: No
  - `unknown`: Desconocido
- **¿Ictus previo?** (`priorStroke`, `sel`)
  - `yes`: Sí
  - `no`: No
  - `unknown`: Desconocido
- **¿Insuficiencia cardíaca previa?** (`priorHF`, `sel`)
  - `yes`: Sí
  - `no`: No
  - `unknown`: Desconocido
- **¿Intervención coronaria percutánea previa?** (`priorPCI`, `sel`)
  - `yes`: Sí
  - `no`: No
  - `unknown`: Desconocido
- **¿Cirugía de revascularización coronaria previa?** (`priorCABG`, `sel`)
  - `yes`: Sí
  - `no`: No
  - `unknown`: Desconocido
- **¿Fibrilación auricular previa?** (`atrialFibrillation`, `sel`)
  - `yes`: Sí
  - `no`: No
  - `unknown`: Desconocido
- **¿Estado aparentemente sano en la evaluación basal confirmado?** (`apparentlyHealthy`, `sel`)
  - `yes`: Sí
  - `no`: No
  - `unknown`: Desconocido
- **¿Uso del modelo histórico para investigación confirmado?** (`historicalResearchConfirmed`, `sel`)
  - `yes`: Sí
  - `no`: No
  - `unknown`: Desconocido

## Límites y revisión

Las categorías poblacionales son las dos categorías históricas estadounidenses de la fuente; no sustituir silenciosamente otros grupos. Edad: 40–79 años; colesterol total: 130–320 mg/dL; HDL: 20–100 mg/dL; presión sistólica: 90–200 mmHg. Los tres límites de laboratorio/presión son convenciones del estimador oficial antiguo. Responder explícitamente antecedentes y confirmaciones; las respuestas desconocidas o exclusiones no producen una estimación. El ACC indica que el riesgo a diez años derivado de PCE ya no está respaldado por la política clínica/directrices actuales. Es un candidato de investigación histórica, no PREVENT, consejo terapéutico ni validación clínica. Un ejemplo publicado de varón blanco sigue siendo discrepante: la ecuación con coeficientes publicados redondea a 5,4%, pero la tabla imprime 5,3%. No se cambiaron coeficientes para ocultar la diferencia. No se han obtenido permisos de distribución ni se ha realizado revisión clínica/profesional.

El ACC indica que el riesgo a diez años derivado de PCE ya no está respaldado por la política clínica/directrices actuales. Es un candidato de investigación histórica, no PREVENT, consejo terapéutico ni validación clínica. Un ejemplo publicado de varón blanco sigue siendo discrepante: la ecuación con coeficientes publicados redondea a 5,4%, pero la tabla imprime 5,3%. No se cambiaron coeficientes para ocultar la diferencia. No se han obtenido permisos de distribución ni se ha realizado revisión clínica/profesional.

Las comprobaciones técnicas utilizan datos sintéticos. No se han realizado una revisión clínica independiente ni una revisión profesional de las traducciones.

## Ejecutar con datos sintéticos

```sh
node cli.cjs examples/input.json es
```

## Resultados

- Estimación histórica a 10 años (%)
<p>Probabilidad a 10 años = 1 − S₀<sup>exp(ΣβX − media)</sup>; porcentaje = 100 × probabilidad. X usa logaritmos naturales e interacciones de la columna de población/sexo publicada. Se conserva la precisión publicada de los coeficientes; mostrar un decimal no cambia el resultado bruto.</p>

## Fuente y derechos

- https://doi.org/10.1161/01.cir.0000437741.48606.98
- https://www.heart.org/-/media/Data-Import/downloadables/0/D/A/2013-AHA-ACC-Cardiovascular-Risk-Guidelines-UCM_464291.pdf
- https://tools.acc.org/cvd-risk-estimator-plus/

[RIGHTS-SCOPE.md](../RIGHTS-SCOPE.md) · [test receipts](../evidence/)
