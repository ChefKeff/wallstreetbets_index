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

## Stocks used with predictions
|    | **Ticker** | **Precision**       |
|----|------------|---------------------|
| 0  | IQ         | 0.5675675675675675  |
| 1  | GM         | 0.4695121951219512  |
| 2  | ES         | 0.5261437908496732  |
| 3  | GL         | 0.5627240143369175  |
| 4  | PYPL       | 0.574468085106383   |
| 5  | IP         | 0.5030674846625767  |
| 6  | KO         | 0.5555555555555556  |
| 7  | MSFT       | 0.535483870967742   |
| 8  | CMG        | 0.5318181818181819  |
| 9  | IT         | 0.5144927536231884  |
| 10 | EA         | 0.48226950354609927 |
| 11 | ATVI       | 0.5061224489795918  |
| 12 | AMD        | 0.4719626168224299  |
| 13 | NVDA       | 0.526984126984127   |
| 14 | IMO        | 0.5846994535519126  |
| 15 | USO        | 0.5325443786982249  |
| 16 | HD         | 0.46853146853146854 |
| 17 | GLD        | 0.5594059405940595  |
| 18 | ONE        | 0.0                 |
| 19 | ET         | 0.47058823529411764 |
| 20 | SO         | 0.543859649122807   |
| 21 | HR         | 0.5882352941176471  |
| 22 | IWM        | 0.5299145299145299  |
| 23 | CC         | 0.48704663212435234 |
| 24 | ARE        | 0.5678571428571428  |
| 25 | NOW        | 0.5781818181818181  |
| 26 | COST       | 0.47843137254901963 |
| 27 | NG         | 0.41379310344827586 |
| 28 | AMC        | 0.42857142857142855 |
| 29 | GME        | 0.4186046511627907  |
| 30 | SNAP       | 0.4587628865979381  |
| 31 | SBUX       | 0.5622119815668203  |
| 32 | QQQ        | 0.5588235294117647  |
| 33 | MCD        | 0.5555555555555556  |
| 34 | AMZN       | 0.5353535353535354  |
| 35 | INTC       | 0.4724770642201835  |
| 36 | ANY        | 1.0                 |
| 37 | TLRY       | 0.0                 |
| 38 | AM         | 0.375               |
| 39 | BA         | 0.5140845070422535  |
| 40 | WW         | 0.5454545454545454  |
| 41 | SMH        | 0.5798319327731093  |
| 42 | UI         | 0.5163043478260869  |
| 43 | MO         | 0.45161290322580644 |
| 44 | BB         | 0.5                 |
| 45 | EDIT       | 0.43902439024390244 |
| 46 | DTE        | 0.4797979797979798  |
| 47 | OR         | 0.5104895104895105  |
| 48 | CGC        | 0.5454545454545454  |
| 49 | TQQQ       | 0.5782747603833865  |
| 50 | BAC        | 0.501628664495114   |
