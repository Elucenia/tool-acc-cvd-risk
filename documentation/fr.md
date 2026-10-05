# PCE2013 · modèle historique

Reproduit l’équation historique de 2013 pour un premier infarctus non mortel, décès coronarien ou AVC mortel/non mortel sur dix ans. N’estime ni l’insuffisance cardiaque, ni le risque au cours de la vie, ni les effets d’un traitement.

## Méthode et édition

PCE2013 · coefficients publiés dans l’Annexe 4, Tableaux A/B ; modèle historique

## Entrées

- **Sexe dans l’équation publiée** (`sex`, `sel`)
  - `female`: Féminin
  - `male`: Masculin
- **Groupe de population de dérivation** (`population`, `sel`)
  - `nonHispanicWhite`: Personne blanche non hispanique
  - `nonHispanicAfricanAmerican`: Personne afro-américaine non hispanique
  - `unsupported`: Autre groupe / non déterminé
- **Âge** (`ageYears`, `num`) — ans [40–79]
- **Cholestérol total** (`totalCholesterolMgDl`, `num`) — mg/dL [130–320]
- **Cholestérol HDL** (`hdlCholesterolMgDl`, `num`) — mg/dL [20–100]
- **Pression artérielle systolique** (`systolicBpMmHg`, `num`) — mmHg [90–200]
- **Traitement antihypertenseur actuel ?** (`treatedBp`, `sel`)
  - `yes`: Oui
  - `no`: Non
- **Tabagisme actuel ?** (`smoker`, `sel`)
  - `yes`: Oui
  - `no`: Non
- **Diabète ?** (`diabetes`, `sel`)
  - `yes`: Oui
  - `no`: Non
- **Infarctus du myocarde antérieur ?** (`priorMI`, `sel`)
  - `yes`: Oui
  - `no`: Non
  - `unknown`: Inconnu
- **AVC antérieur ?** (`priorStroke`, `sel`)
  - `yes`: Oui
  - `no`: Non
  - `unknown`: Inconnu
- **Insuffisance cardiaque antérieure ?** (`priorHF`, `sel`)
  - `yes`: Oui
  - `no`: Non
  - `unknown`: Inconnu
- **Intervention coronarienne percutanée antérieure ?** (`priorPCI`, `sel`)
  - `yes`: Oui
  - `no`: Non
  - `unknown`: Inconnu
- **Pontage aorto-coronarien antérieur ?** (`priorCABG`, `sel`)
  - `yes`: Oui
  - `no`: Non
  - `unknown`: Inconnu
- **Fibrillation atriale antérieure ?** (`atrialFibrillation`, `sel`)
  - `yes`: Oui
  - `no`: Non
  - `unknown`: Inconnu
- **État apparemment sain confirmé lors de l’évaluation initiale ?** (`apparentlyHealthy`, `sel`)
  - `yes`: Oui
  - `no`: Non
  - `unknown`: Inconnu
- **Utilisation du modèle historique pour la recherche confirmée ?** (`historicalResearchConfirmed`, `sel`)
  - `yes`: Oui
  - `no`: Non
  - `unknown`: Inconnu

## Limites et révision

Les catégories de population sont les deux catégories américaines historiques de la source ; ne pas leur substituer silencieusement d’autres groupes. Âge : 40–79 ans ; cholestérol total : 130–320 mg/dL ; HDL : 20–100 mg/dL ; pression systolique : 90–200 mmHg. Les trois limites biologiques/de pression sont des conventions de l’ancien estimateur officiel. Répondre explicitement aux antécédents et confirmations ; une réponse inconnue ou une exclusion ne produit pas d’estimation. L’ACC indique que le risque à dix ans issu de PCE n’est plus soutenu par la politique clinique/les recommandations actuelles. Il s’agit d’un candidat de recherche historique, non de PREVENT, d’un conseil thérapeutique ou d’une validation clinique. Un exemple publié pour un homme blanc reste divergent : l’équation aux coefficients publiés s’arrondit à 5,4 %, alors que le tableau indique 5,3 %. Aucun coefficient n’a été modifié pour masquer l’écart. Autorisation de distribution non obtenue ; revue clinique/professionnelle non réalisée.

L’ACC indique que le risque à dix ans issu de PCE n’est plus soutenu par la politique clinique/les recommandations actuelles. Il s’agit d’un candidat de recherche historique, non de PREVENT, d’un conseil thérapeutique ou d’une validation clinique. Un exemple publié pour un homme blanc reste divergent : l’équation aux coefficients publiés s’arrondit à 5,4 %, alors que le tableau indique 5,3 %. Aucun coefficient n’a été modifié pour masquer l’écart. Autorisation de distribution non obtenue ; revue clinique/professionnelle non réalisée.

Les vérifications techniques utilisent des données synthétiques. La révision clinique indépendante et la révision professionnelle des traductions n’ont pas été effectuées.

## Exécuter avec des données synthétiques

```sh
node cli.cjs examples/input.json fr
```

## Résultats

- Estimation historique à 10 ans (%)
<p>Probabilité à 10 ans = 1 − S₀<sup>exp(ΣβX − moyenne)</sup> ; pourcentage = 100 × probabilité. X utilise les logarithmes naturels et les interactions de la colonne population/sexe publiée. La précision publiée des coefficients est conservée ; l’affichage à une décimale ne modifie pas le résultat brut.</p>

## Source et droits

- https://doi.org/10.1161/01.cir.0000437741.48606.98
- https://www.heart.org/-/media/Data-Import/downloadables/0/D/A/2013-AHA-ACC-Cardiovascular-Risk-Guidelines-UCM_464291.pdf
- https://tools.acc.org/cvd-risk-estimator-plus/

[RIGHTS-SCOPE.md](../RIGHTS-SCOPE.md) · [test receipts](../evidence/)
