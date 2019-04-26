# GUI-RPD-Discounting-Observation Errorsの説明
繰り返し囚人のジレンマゲームの戦略が，割引因子や観測エラーによってどのような影響を受けるのか，このツールを使うことによって，理解を深めることができる．

- <img src="https://latex.codecogs.com/gif.latex?{\bf%20p}=(p_1,p_2,p_3,p_4),p_0"> は自分（縦軸）の戦略
- <img src="https://latex.codecogs.com/gif.latex?\epsilon,\xi">はそれぞれ一方のみがエラーする確率，両方エラーする確率
- <img src="https://latex.codecogs.com/gif.latex?w">は割引因子　（w=1のときは割引なし）
- 相手（横軸）の戦略 <img src="https://latex.codecogs.com/gif.latex?{\bf%20q}">はランダム

自分の戦略を1つに決め，ランダムに決めた相手の1,000+2戦略に対して，それぞれゲームを行った時の利得関係を表す．
相手の+2戦略分は，ALLC戦略（青点）とALLD（赤点）である．
## 操作方法
### スライダー
- 計算方法の切り替え
  - (0)Detは本研究で見つけた行列式で計算する方法，(1)はHilbe et al.,2015,GBEで示された逆行列の形で計算する方法である
- 割引因子<img src="https://latex.codecogs.com/gif.latex?w">，エラー率<img src="https://latex.codecogs.com/gif.latex?\epsilon,\xi">は，スライダーで変更できる
- 戦略<img src="https://latex.codecogs.com/gif.latex?{\bf%20p}=(p_1,p_2,p_3,p_4),p_0=1">の値もスライダーから変更できる．1,000分の1単位で値を変えることができる．
### ボタン
- Other Opponent
  - 相手の戦略<img src="https://latex.codecogs.com/gif.latex?{\bf%20q}">の値を別のランダムな値に変更する．
- TRPS 5310
  - <img src="https://latex.codecogs.com/gif.latex?(T,R,P,S)=(1.5,1,0,-0.5)">から<img src="https://latex.codecogs.com/gif.latex?(T,R,P,S)=(5,3,1,0)">に変更する．
- Save Fig
  - 任意の場所に今表示している図をPNG形式で保存する．
- Quit
  - ツールを終了する．

## UIの例
### 条件
- <img src="https://latex.codecogs.com/gif.latex?(T,R,P,S)=(1.5,1,0,-0.5)">
- <img src="https://latex.codecogs.com/gif.latex?w=1">　（割引なし）
- <img src="https://latex.codecogs.com/gif.latex?%28%5Cepsilon%2C%5Cxi%29%3D%280%2C0%29">　（エラーなし）
- <img src="https://latex.codecogs.com/gif.latex?{\bf%20p}=(1,0,0,1),%20p_0=1"> （WSLS戦略）

※相手がALLCのときは，定常分布がなく計算できないので，青点が表示されない．

![wsls strategy](https://github.com/azm17/RPD/blob/master/wsls.PNG "wsls")
