# Herding vs WOC in stock prediction

Hello and welcome to the repo for my thesis in economics at Uppsala University. 
The thesis looks at herding vs WOC in predicting stock market returns - using sentiment from r/wallstreetbets as the herding party and Google Trends data as the WOC component. 

The final thesis can be read [here](https://klockren.nu).

Dependencies
* [Pandas](https://pandas.pydata.org/)
* [pytrends](https://pypi.org/project/pytrends/)
* [yfinance](https://pypi.org/project/yfinance/)
* [sklearn](https://scikit-learn.org/stable/)
* [numpy](https://numpy.org/)

The r/wallstreetbets sentiment used is collected from [ApeWisdom](https://apewisdom.io/).

Feel free to reach out if you have any questions - either through my [website](https://niklasnorinder.herokuapp.com) or just by shooting me an [email](mailto:niklas.norinder.4686@student.uu.se).

/Niklas 🆒

## Stocks used with precision
|      |Ticker   |Precision   |
|------|---------|------------|
|0     |TLRY     |0           |
|1     |AM       |0.375       |
|2     |WW       |0.5454545455|
|3     |BA       |0.514084507 |
|4     |UI       |0.5163043478|
|5     |SMH      |0.5798319328|
|6     |MO       |0.4516129032|
|7     |OR       |0.5104895105|
|8     |DTE      |0.4797979798|
|9     |BB       |0.5         |
|10    |CGC      |0.5454545455|
|11    |EDIT     |0.4390243902|
|12    |TQQQ     |0.5782747604|
|13    |BAC      |0.5016286645|
|14    |CC       |0.4870466321|
|15    |ARE      |0.5678571429|
|16    |NOW      |0.5781818182|
|17    |COST     |0.4784313725|
|18    |NG       |0.4137931034|
|19    |SNAP     |0.4587628866|
|20    |GME      |0.4186046512|
|21    |SBUX     |0.5622119816|
|22    |AMC      |0.4285714286|
|23    |INTC     |0.4724770642|
|24    |AMZN     |0.5353535354|
|25    |MCD      |0.5555555556|
|26    |QQQ      |0.5588235294|
|27    |ANY      |1           |
|28    |IQ       |0.5675675676|
|29    |GM       |0.4695121951|
|30    |GL       |0.5627240143|
|31    |ES       |0.5261437908|
|32    |KO       |0.5555555556|
|33    |IP       |0.5030674847|
|34    |MSFT     |0.535483871 |
|35    |PYPL     |0.5744680851|
|36    |CMG      |0.5318181818|
|37    |IT       |0.5144927536|
|38    |ATVI     |0.506122449 |
|39    |EA       |0.4822695035|
|40    |AMD      |0.4719626168|
|41    |NVDA     |0.526984127 |
|42    |ONE      |0           |
|43    |IMO      |0.5846994536|
|44    |GLD      |0.5594059406|
|45    |USO      |0.5325443787|
|46    |HD       |0.4685314685|
|47    |ET       |0.4705882353|
|48    |HR       |0.5882352941|
|49    |SO       |0.5438596491|
|50    |IWM      |0.5299145299|
|51    |FANG     |0.4730538922|
|52    |OUT      |0.4564102564|
|53    |FB       |0.5179153094|
|54    |TWTR     |0.5037037037|
|55    |UVXY     |0           |
|56    |IBM      |0.4615384615|
|57    |GS       |0.5268292683|
|58    |LULU     |0.5462962963|
|59    |GE       |0.4554455446|
|60    |ALL      |0.5901060071|
|61    |RE       |0.5342465753|
|62    |DIS      |0.4961832061|
|63    |ACB      |0.5806451613|
|64    |NFLX     |0.5374592834|
|65    |CVS      |0.4915254237|
|66    |JPM      |0.4980392157|
|67    |TSLA     |0.5072463768|
|68    |SPY      |0.5441595442|
|69    |GOOGL    |0.518115942 |
|70    |USD      |0.5423197492|
|71    |BIG      |0.46875     |
|72    |SP       |0.4788732394|
|73    |SQ       |0.5141700405|
|74    |JD       |0.4705882353|
|75    |SHOP     |0.548       |
|76    |RAD      |0           |
|77    |GOOG     |0.4846153846|
|78    |VZ       |0.57        |
|79    |TD       |0.5101351351|
