# PCE2013 · 历史模型

重现 2013 年历史方程，估计十年内首次非致死性心肌梗死、冠心病死亡或致死性／非致死性卒中。不估计心力衰竭、终生风险或治疗效果。

## 方法与版本

PCE2013 · 附录 4 表 A/B 中发表的系数；历史模型

## 输入

- **已发表方程使用的性别** (`sex`, `sel`)
  - `female`: 女性
  - `male`: 男性
- **模型推导人群组别** (`population`, `sel`)
  - `nonHispanicWhite`: 非西班牙裔白人
  - `nonHispanicAfricanAmerican`: 非西班牙裔非洲裔美国人
  - `unsupported`: 其他组别／未确定
- **年龄** (`ageYears`, `num`) — 岁 [40–79]
- **总胆固醇** (`totalCholesterolMgDl`, `num`) — mg/dL [130–320]
- **HDL 胆固醇** (`hdlCholesterolMgDl`, `num`) — mg/dL [20–100]
- **收缩压** (`systolicBpMmHg`, `num`) — mmHg [90–200]
- **目前接受降压治疗？** (`treatedBp`, `sel`)
  - `yes`: 是
  - `no`: 否
- **目前吸烟？** (`smoker`, `sel`)
  - `yes`: 是
  - `no`: 否
- **糖尿病？** (`diabetes`, `sel`)
  - `yes`: 是
  - `no`: 否
- **既往心肌梗死？** (`priorMI`, `sel`)
  - `yes`: 是
  - `no`: 否
  - `unknown`: 未知
- **既往卒中？** (`priorStroke`, `sel`)
  - `yes`: 是
  - `no`: 否
  - `unknown`: 未知
- **既往心力衰竭？** (`priorHF`, `sel`)
  - `yes`: 是
  - `no`: 否
  - `unknown`: 未知
- **既往经皮冠状动脉介入治疗？** (`priorPCI`, `sel`)
  - `yes`: 是
  - `no`: 否
  - `unknown`: 未知
- **既往冠状动脉旁路移植术？** (`priorCABG`, `sel`)
  - `yes`: 是
  - `no`: 否
  - `unknown`: 未知
- **既往心房颤动？** (`atrialFibrillation`, `sel`)
  - `yes`: 是
  - `no`: 否
  - `unknown`: 未知
- **已确认基线评估时表面健康的状态？** (`apparentlyHealthy`, `sel`)
  - `yes`: 是
  - `no`: 否
  - `unknown`: 未知
- **已确认将此历史模型用于研究？** (`historicalResearchConfirmed`, `sel`)
  - `yes`: 是
  - `no`: 否
  - `unknown`: 未知

## 限制与审查

人群分类是来源中的两种历史美国分类；不得默认为其他人群替代模型。年龄：40–79 岁；总胆固醇：130–320 mg/dL；HDL：20–100 mg/dL；收缩压：90–200 mmHg。三个检验／血压范围是旧版官方估计器的输入约定。须明确回答病史及确认项；未知回答或排除条件不产生估计。 ACC 说明，PCE 得出的十年风险已不再受到现行临床政策／指南支持。本实现是历史研究候选，不是 PREVENT、治疗建议或临床验证。一个已发表的白人男性示例仍有差异：用发表系数计算并舍入为 5.4%，但表中印为 5.3%。未更改系数来掩盖差异。尚未完成分发许可及临床／专业审核。

ACC 说明，PCE 得出的十年风险已不再受到现行临床政策／指南支持。本实现是历史研究候选，不是 PREVENT、治疗建议或临床验证。一个已发表的白人男性示例仍有差异：用发表系数计算并舍入为 5.4%，但表中印为 5.3%。未更改系数来掩盖差异。尚未完成分发许可及临床／专业审核。

技术检查使用合成数据。尚未开展独立临床审查和专业翻译审查。

## 使用合成数据运行

```sh
node cli.cjs examples/input.json zh
```

## 结果

- 历史模型的 10 年估计 (%)
<p>10 年概率 = 1 − S₀<sup>exp(ΣβX − 均值)</sup>；百分比 = 100 × 概率。X 使用发表的人群／性别列中的自然对数和交互项。保留发表系数的精度；显示一位小数不改变原始结果。</p>

## 来源与权利

- https://doi.org/10.1161/01.cir.0000437741.48606.98
- https://www.heart.org/-/media/Data-Import/downloadables/0/D/A/2013-AHA-ACC-Cardiovascular-Risk-Guidelines-UCM_464291.pdf
- https://tools.acc.org/cvd-risk-estimator-plus/

[RIGHTS-SCOPE.md](../RIGHTS-SCOPE.md) · [test receipts](../evidence/)
