# PCE2013 · 歴史的モデル

2013年の歴史的な式を再現し、10年間の初回非致死性心筋梗塞、冠動脈疾患による死亡、致死性・非致死性脳卒中を推定する。心不全、生涯リスク、治療効果は推定しない。

## 方法と版

PCE2013 · 付録4の表A/Bに公表された係数；歴史的モデル

## 入力

- **公表された式における性別** (`sex`, `sel`)
  - `female`: 女性
  - `male`: 男性
- **モデル導出集団の群** (`population`, `sel`)
  - `nonHispanicWhite`: 非ヒスパニック系白人
  - `nonHispanicAfricanAmerican`: 非ヒスパニック系アフリカ系米国人
  - `unsupported`: ほかの群／未確定
- **年齢** (`ageYears`, `num`) — 歳 [40–79]
- **総コレステロール** (`totalCholesterolMgDl`, `num`) — mg/dL [130–320]
- **HDLコレステロール** (`hdlCholesterolMgDl`, `num`) — mg/dL [20–100]
- **収縮期血圧** (`systolicBpMmHg`, `num`) — mmHg [90–200]
- **現在の降圧治療？** (`treatedBp`, `sel`)
  - `yes`: はい
  - `no`: いいえ
- **現在の喫煙？** (`smoker`, `sel`)
  - `yes`: はい
  - `no`: いいえ
- **糖尿病？** (`diabetes`, `sel`)
  - `yes`: はい
  - `no`: いいえ
- **心筋梗塞の既往？** (`priorMI`, `sel`)
  - `yes`: はい
  - `no`: いいえ
  - `unknown`: 不明
- **脳卒中の既往？** (`priorStroke`, `sel`)
  - `yes`: はい
  - `no`: いいえ
  - `unknown`: 不明
- **心不全の既往？** (`priorHF`, `sel`)
  - `yes`: はい
  - `no`: いいえ
  - `unknown`: 不明
- **経皮的冠動脈インターベンションの既往？** (`priorPCI`, `sel`)
  - `yes`: はい
  - `no`: いいえ
  - `unknown`: 不明
- **冠動脈バイパス術の既往？** (`priorCABG`, `sel`)
  - `yes`: はい
  - `no`: いいえ
  - `unknown`: 不明
- **心房細動の既往？** (`atrialFibrillation`, `sel`)
  - `yes`: はい
  - `no`: いいえ
  - `unknown`: 不明
- **ベースライン評価時に見かけ上健康であることを確認済み？** (`apparentlyHealthy`, `sel`)
  - `yes`: はい
  - `no`: いいえ
  - `unknown`: 不明
- **歴史的モデルを研究に使用することを確認済み？** (`historicalResearchConfirmed`, `sel`)
  - `yes`: はい
  - `no`: いいえ
  - `unknown`: 不明

## 限界と検討

集団分類は出典の歴史的な米国の2分類で、ほかの集団に暗黙に置き換えない。年齢40–79歳、総コレステロール130–320 mg/dL、HDL 20–100 mg/dL、収縮期血圧90–200 mmHg。3つの検査値・血圧範囲は旧公式推定器の入力規約。既往と確認項目に明示的に回答する。不明な回答や除外条件では推定を出さない。 ACCは、PCEによる10年間のリスクが現行の臨床方針・ガイドラインでは支持されなくなったと説明している。これは歴史的研究の候補であり、PREVENT、治療助言、臨床的検証ではない。公表された白人男性の1例には不一致が残る。公表係数による式を丸めると5.4%だが、表には5.3%とある。不一致を隠す係数変更は行っていない。配布許可と臨床・専門職によるレビューは未実施。

ACCは、PCEによる10年間のリスクが現行の臨床方針・ガイドラインでは支持されなくなったと説明している。これは歴史的研究の候補であり、PREVENT、治療助言、臨床的検証ではない。公表された白人男性の1例には不一致が残る。公表係数による式を丸めると5.4%だが、表には5.3%とある。不一致を隠す係数変更は行っていない。配布許可と臨床・専門職によるレビューは未実施。

技術的な確認には合成データを使用しています。独立した臨床レビューと専門家による翻訳レビューは実施されていません。

## 合成データで実行

```sh
node cli.cjs examples/input.json ja
```

## 結果

- 歴史的モデルによる10年間の推定 (%)
<p>10年間の確率 = 1 − S₀<sup>exp(ΣβX − 平均)</sup>；百分率 = 100 × 確率。Xは公表された集団・性別列の自然対数と交互作用を使用する。公表係数の精度を保ち、小数1桁の表示は生の結果を変えない。</p>

## 出典と権利

- https://doi.org/10.1161/01.cir.0000437741.48606.98
- https://www.heart.org/-/media/Data-Import/downloadables/0/D/A/2013-AHA-ACC-Cardiovascular-Risk-Guidelines-UCM_464291.pdf
- https://tools.acc.org/cvd-risk-estimator-plus/

[RIGHTS-SCOPE.md](../RIGHTS-SCOPE.md) · [test receipts](../evidence/)
