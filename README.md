# 🧑‍🤝‍🧑 Herding 🧑‍🤝‍🧑 vs 🧠 WOC 🧠 in stock prediction

Hello and welcome to the repo for my thesis in economics at Uppsala University. 
The thesis looks at herding vs WOC in predicting stock market returns - using sentiment from r/wallstreetbets as the herding party and Google Trends data as the WOC component. 

The final thesis can be read [here](http://uu.diva-portal.org/smash/record.jsf?aq2=%5B%5B%5D%5D&c=5&af=%5B%5D&searchType=LIST_LATEST&sortOrder2=title_sort_asc&query=&language=en&pid=diva2%3A1682434&aq=%5B%5B%5D%5D&sf=all&aqe=%5B%5D&sortOrder=author_sort_asc&onlyFullText=false&noOfRows=50&dswid=-4660).

Dependencies
* [Pandas](https://pandas.pydata.org/)
* [pytrends](https://pypi.org/project/pytrends/)
* [yfinance](https://pypi.org/project/yfinance/)
* [sklearn](https://scikit-learn.org/stable/)
* [numpy](https://numpy.org/)

The r/wallstreetbets sentiment used is collected from [ApeWisdom](https://apewisdom.io/).

Feel free to reach out if you have any questions - either through my [website](https://niklasnorinder.se) or just by shooting me an [email](mailto:niklas.norinder.4686@student.uu.se).

Special thanks to 
* The wonderful people at [ApeWisdom](https://apewisdom.io/) - helping me get the historical data from the stocks.
* My supervisor Peter Ek for always providing great feedback.
* Fredrik Nilsson for listening to my non-stop rambling about machine learning.

/Niklas Norinder 

## Stocks used with precision
|Index |Ticker|Precision WSB RFC|Precision WSB MLP|Precision Google Trends RFC|Precision Google Trends MLP|Precision WSB & Trends RFC|Precision WSB & Trends MLP|
|------|------|-----------------|-----------------|---------------------------|---------------------------|--------------------------|--------------------------|
|0     |AM    |0.3606557377     |0                |0.4423076923               |0.4285714286               |0.425                     |0                         |
|1     |BA    |0.4388489209     |0.4588235294     |0.4882352941               |0.5111111111               |0.4347826087              |0.4585635359              |
|2     |WW    |0.6              |0.6              |0.4915254237               |0.5341614907               |0.5982905983              |0.5416666667              |
|3     |MO    |0.4836601307     |0.5467625899     |0.5304347826               |0                          |0.5371900826              |0.4976076555              |
|4     |UI    |0.5279187817     |0.510373444      |0.5189873418               |0.5090909091               |0.5471698113              |0.5432692308              |
|5     |SMH   |0.5784313725     |0.5731707317     |0.5482233503               |0.5780590717               |0.5817307692              |0.5731707317              |
|6     |DTE   |0.4976303318     |0.4867924528     |0.5081967213               |0.4908424908               |0.4957264957              |0.5021276596              |
|7     |BB    |0.3333333333     |0                |0.4857142857               |0.5                        |0.4285714286              |0                         |
|8     |EDIT  |0.4338624339     |0.5555555556     |0.472392638                |0                          |0.4350649351              |0.4417177914              |
|9     |OR    |0.4794520548     |0.4347826087     |0.506097561                |0.5                        |0.45                      |0.4509803922              |
|10    |TQQQ  |0.590443686      |0.5815384615     |0.5948905109               |0.5815384615               |0.5833333333              |0.5815384615              |
|11    |CGC   |0.4464285714     |0                |0.4222222222               |0                          |0.4204545455              |0                         |
|12    |BAC   |0.5058823529     |0.5104477612     |0.51953125                 |0.5077720207               |0.5163934426              |0.4985673352              |
|13    |CC    |0.5              |0.4856115108     |0.4587155963               |0.487804878                |0.5204081633              |0.4976525822              |
|14    |ARE   |0.5729927007     |0.5686900958     |0.5518672199               |0.5668789809               |0.5703125                 |0.5695364238              |
|15    |NOW   |0.5521235521     |0.5783475783     |0.6060606061               |0.3333333333               |0.5653846154              |0.5743440233              |
|16    |COST  |0.4672131148     |0.480620155      |0.4817813765               |0.480620155                |0.4655870445              |0.480620155               |
|17    |NG    |0.4511278195     |0                |0.4945054945               |0.488372093                |0.4489795918              |0.6                       |
|18    |AMC   |0.25             |0                |0.4583333333               |0                          |0.4074074074              |0                         |
|19    |SBUX  |0.5707070707     |0.54             |0.5632183908               |0.5397350993               |0.5483870968              |0.5436507937              |
|20    |GME   |0.4693877551     |1                |0.5061728395               |0                          |0.452173913               |0                         |
|21    |SNAP  |0.48             |0.4693877551     |0.4242424242               |0.4210526316               |0.4773869347              |0.5046728972              |
|22    |QQQ   |0.5688073394     |0.5604395604     |0.5806451613               |0.5625                     |0.5649546828              |0.5621468927              |
|23    |MCD   |0.5654008439     |0.5632911392     |0.5683060109               |0.5514705882               |0.5265700483              |0.5670103093              |
|24    |AMZN  |0.5167785235     |0.5170731707     |0.5482758621               |0.53                       |0.5349544073              |0.5204819277              |
|25    |ANY   |0.5              |0                |0                          |0                          |0.5                       |0                         |
|26    |INTC  |0.5047619048     |0.498470948      |0.5144508671               |0.5120772947               |0.5482233503              |0.5411764706              |
|27    |IQ    |0.52             |0                |0.5178571429               |0                          |0.5                       |0.6923076923              |
|28    |GM    |0.4375           |0.552238806      |0.4785714286               |0.5652173913               |0.4184397163              |0.5                       |
|29    |GL    |0.5405405405     |0.5352112676     |0.5144694534               |0.5352112676               |0.5382059801              |0.5352112676              |
|30    |ES    |0.5373134328     |0.5035460993     |0.5296610169               |0.5087209302               |0.5107142857              |0.5563380282              |
|31    |PYPL  |0.5497835498     |0.5615384615     |0.5772727273               |0.5619834711               |0.5391705069              |0.5351351351              |
|32    |IP    |0.5766423358     |0.5625           |0.45                       |0.5                        |0.5277777778              |0.5459770115              |
|33    |KO    |0.527607362      |0.5287356322     |0.5287958115               |0.5241635688               |0.5294117647              |0.5241635688              |
|34    |MSFT  |0.5396825397     |0.5422343324     |0.554517134                |0.5322580645               |0.5498281787              |0.5480225989              |
|35    |IT    |0.5381679389     |0.5289672544     |0.524137931                |0.5289672544               |0.5703125                 |0.5548780488              |
|36    |CMG   |0.5317919075     |0.5325670498     |0.5389221557               |0                          |0.5470588235              |0.6153846154              |
|37    |ATVI  |0.4692307692     |0.494047619      |0.5161290323               |0.4897959184               |0.5162601626              |0.4836065574              |
|38    |AMD   |0.5164835165     |0.4889705882     |0.5223880597               |0.4601226994               |0.4894736842              |0.4705882353              |
|39    |EA    |0.5260115607     |0.5133928571     |0.4836956522               |0.5070422535               |0.509202454               |0.5                       |
|40    |NVDA  |0.5118644068     |0.530952381      |0.525083612                |0.5378590078               |0.5173501577              |0.5180055402              |
|41    |GLD   |0.5619834711     |0.5634920635     |0.5845070423               |0.5729927007               |0.5642857143              |0.5634920635              |
|42    |ET    |0.5043478261     |0                |0.4552845528               |0.4384615385               |0.488372093               |0                         |
|43    |IMO   |0.5090909091     |0.5922330097     |0.5185185185               |0.4                        |0.5212121212              |0.5222222222              |
|44    |ONE   |0.5              |0                |0                          |0                          |0.75                      |0                         |
|45    |HD    |0.4603773585     |0.475862069      |0.4812030075               |0.47                       |0.4746376812              |0.4785714286              |
|46    |USO   |0.5              |0.5285714286     |0.5449101796               |0.4375                     |0.5508982036              |0.5355191257              |
|47    |HR    |0.527027027      |0.5              |0.5128205128               |0.5                        |0.5348837209              |0.2857142857              |
|48    |SO    |0.5310077519     |0.5321100917     |0.5714285714               |0.5294117647               |0.4978902954              |0.5495867769              |
|49    |IWM   |0.5575221239     |0.5501858736     |0.5801104972               |0.5501858736               |0.5631578947              |0.5693779904              |
|50    |OUT   |0.3916666667     |0.5287356322     |0.5460992908               |0.4701492537               |0.4273504274              |0.4505494505              |
|51    |FANG  |0.488            |0.4846625767     |0.4892086331               |0.4615384615               |0.5338345865              |0.4746835443              |
|52    |TWTR  |0.55             |0                |0.5207100592               |0.5094339623               |0.5290322581              |0.6363636364              |
|53    |IBM   |0.5029239766     |0.4618473896     |0.4536082474               |0.3666666667               |0.4892473118              |0.4416666667              |
|54    |FB    |0.4956896552     |0.5026455026     |0.5063829787               |0.4929971989               |0.5025906736              |0.5061349693              |
|55    |UVXY  |0                |0.5              |0.5                        |0                          |0.6666666667              |0                         |
|56    |LULU  |0.5142857143     |0.5336538462     |0.5482233503               |0.5257352941               |0.5481927711              |0.522556391               |
|57    |GS    |0.5119047619     |0.5256410256     |0.5118483412               |0.5169811321               |0.5053763441              |0.5280235988              |
|58    |ACB   |0.3333333333     |0                |0.5                        |0.5384615385               |0.5                       |0                         |
|59    |RE    |0.4946236559     |0.5239852399     |0.5281385281               |0.5187713311               |0.502994012               |0.5042016807              |
|60    |DIS   |0.5              |0.5696202532     |0.474137931                |0.4166666667               |0.5303030303              |0.5217391304              |
|61    |GE    |0.4025974026     |0.4318181818     |0.3921568627               |0                          |0.4235294118              |0.4457831325              |
|62    |ALL   |0.5800711744     |0.6027874564     |0.532                      |0.5670103093               |0.5974025974              |0.5892857143              |
|63    |NFLX  |0.51171875       |0.5224274406     |0.5490196078               |0.5238095238               |0.5375                    |0.5269461078              |
|64    |JPM   |0.5339366516     |0.5287009063     |0.5401785714               |0.531986532                |0.536036036               |0.5201465201              |
|65    |CVS   |0.475862069      |0.5147058824     |0.4642857143               |0.5190839695               |0.4927536232              |0.5042735043              |
|66    |TSLA  |0.5257352941     |0.5178571429     |0.5209125475               |0.5166666667               |0.5207373272              |0.536                     |
|67    |USD   |0.5342960289     |0.5459183673     |0.5583596215               |0.5459183673               |0.5328719723              |0.5459183673              |
|68    |SPY   |0.55625          |0.5373493976     |0.5367847411               |0.5386416862               |0.5527950311              |0.5354330709              |
|69    |BIG   |0.4468085106     |0.3913043478     |0.5384615385               |0                          |0.4912280702              |0.480620155               |
|70    |GOOGL |0.5271966527     |0.5292207792     |0.5366795367               |0.5320512821               |0.5152671756              |0.5320512821              |
|71    |SQ    |0.5325670498     |0.5358255452     |0.5134099617               |0.5284552846               |0.5106382979              |0.5369127517              |
|72    |SP    |0.4972677596     |0.4934210526     |0.514619883                |0.4876033058               |0.4855967078              |0.4827586207              |
|73    |GOOG  |0.4697674419     |0.4984984985     |0.4943396226               |0.4984984985               |0.4807692308              |0.4982332155              |
|74    |RAD   |0.8              |0                |0.1818181818               |0                          |0.5714285714              |0                         |
|75    |JD    |0.4444444444     |0.479704797      |0.5027932961               |0.4783950617               |0.4733727811              |0.5023474178              |
|76    |SHOP  |0.5546218487     |0.5379746835     |0.5066666667               |0.5347432024               |0.53307393                |0.5347432024              |
|77    |VZ    |0.4              |0.52             |0.4303797468               |0                          |0.4835164835              |0.3913043478              |
|78    |ON    |0.5721153846     |0.5373563218     |0.504950495                |0.538028169                |0.5538461538              |0.5427350427              |
|79    |AR    |0.5125           |0                |0.4587155963               |0                          |0.5287356322              |0                         |
|80    |TD    |0.4927536232     |0.5203252033     |0.5104895105               |0.5289672544               |0.5056603774              |0.505988024               |
|81    |MS    |0.4686192469     |0.4891640867     |0.4767932489               |0.4891640867               |0.4561403509              |0.474916388               |
|82    |MD    |0.4910714286     |0.48             |0.4631578947               |0                          |0.488                     |0.5                       |
|83    |FOR   |0.4769230769     |0.6              |0.5102040816               |0                          |0.5576923077              |0.6666666667              |
|84    |BABA  |0.515625         |0.4983713355     |0.5108225108               |0.4986449864               |0.5                       |0.4717948718              |
|85    |TGT   |0.5395683453     |0.528            |0.5571428571               |0                          |0.5407407407              |0.5298507463              |
|86    |OI    |0.464            |0.75             |0.4666666667               |0.496124031                |0.4262295082              |0.5238095238              |
|87    |MA    |0.5598455598     |0.5611940299     |0.5708812261               |0.5621301775               |0.5469387755              |0.5610561056              |
|88    |JNUG  |0.475177305      |0                |0.5454545455               |0.5342465753               |0.4230769231              |0                         |
|89    |HAS   |0.4974093264     |0.4939759036     |0.4905660377               |0.5108695652               |0.495                     |0.5108695652              |
|90    |AAPL  |0.5639344262     |0.5768321513     |0.5692307692               |0.5790754258               |0.5698529412              |0.5768321513              |
|91    |WMT   |0.5355191257     |0.5167785235     |0.5173913043               |0.512195122                |0.5566502463              |0.5294117647              |
|92    |IPO   |0.51875          |0.5588235294     |0.5626822157               |0.5588235294               |0.575                     |0.5567282322              |
|93    |LMT   |0.4912280702     |0.5287356322     |0.5394736842               |0                          |0.5                       |0.5                       |
|94    |PSA   |0.5050505051     |0.5547169811     |0.509202454                |0.6363636364               |0.5223880597              |0.5551330798              |
|95    |LINK  |0                |0                |0                          |0                          |0                         |0.3193717277              |
|96    |NOK   |0.4864864865     |0.3333333333     |0.4794520548               |0.5161290323               |0.431372549               |0.406779661               |
|97    |AA    |0.474137931      |0                |0.4946236559               |0                          |0.5273972603              |0.5056179775              |
|98    |MU    |0.5348837209     |0.5242165242     |0.525862069                |0.515037594                |0.512605042               |0.5291005291              |
|99    |CRM   |0.5947712418     |0.5582329317     |0.5743243243               |0.5364238411               |0.5925925926              |0.5361445783              |
|100   |ROKU  |-                |-                |0.5217391304               |0.4615384615               |0.4479166667              |0.5263157895              |
|101   |TLRY  |-                |-                |0.5                        |0                          |0.375                     |0.3333333333              |


## Visualisation of data (unfiltered - with over/underfitting stocks included)
### r/wallstreetbets
![image](https://user-images.githubusercontent.com/73639795/163565557-9694a2f0-ff66-4021-977c-cb3d38d515bf.png)
![image](https://user-images.githubusercontent.com/73639795/163565578-1f6f0a48-035f-4422-84a0-32ad2f126b11.png)
### Google Trends
![image](https://user-images.githubusercontent.com/73639795/163565595-1b26bb7d-d7a3-452d-89b9-4917e3e53200.png)
![image](https://user-images.githubusercontent.com/73639795/163565609-42b694a6-46a6-46eb-9deb-43790b02274b.png)
### r/wallstreetbets and Google Trends combined
![image](https://user-images.githubusercontent.com/73639795/163565678-c0474472-72ed-4bcc-9ba1-ff6aa78453d8.png)
![image](https://user-images.githubusercontent.com/73639795/163565686-0de06dbb-82ad-4dbc-846a-b8904fac2020.png)
