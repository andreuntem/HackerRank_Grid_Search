from collections import Counter

def gridSearch(G, P):

    # flatten pattern
    pattern = ''.join(P)
    list_pattern = list(pattern)
    counter_pattern = Counter(pattern)
    
    # Length grid and pattern
    r_grid, c_grid = len(G), len(G[0])
    r_pat, c_pat = len(P), len(P[0])
    size_pat = r_pat*c_pat
    
    # Check by subgrid:
    found = 'NO'
    for i in  range(r_grid - r_pat + 1):
        for j in range(c_grid - c_pat + 1):
            
            # Define subgrid
            subgrid = [G[i+k][j:j+c_pat] for k in range(r_pat)]
            subgrid = ''.join(subgrid)
            list_subgrid = list(subgrid)
            counter_subgrid = Counter(subgrid)

            if counter_subgrid == counter_pattern:
                diff = [list_pattern[ix] == list_subgrid[ix] for ix in range(size_pat)]
                if all(diff) == True:
                    found = 'YES'
                    break

        if found == 'YES':
            break

    return found

if __name__ == '__main__':
    raw_inp = '''
    100 100
    9257386684621019425511798400214566929283330442113042582543728650560070499147172236294351101413452986
    2775840043800028513104886956562325211096367970895013419536762344399478721292093123586012016119469319
    7093559014521853047929604233604844852647472287169212380955844200116828041625138979533348944170175136
    8596132425215286754477035869045608689588209966549114124341927172258436902591351064439357734398402036
    7390157834223602289310576957798545828219365473199442352622111214565348332217131455523059410263895777
    7920734033393017265401870453890722640184121165083327503709744343784480249870222285240352409973021186
    7069739235117664029474339341701641833322996334378950940925936414850499823091248802528920324499081972
    4765195658929124577616074618312698532510948535105774716840503828696298860551524168319517991550398997
    9489162295044988736549420283000012777078994093340898064976138327514200282558069835335021238557435294
    3571720678454425587290726926285138819427342176801794270971190119637644633517665227270538883533865494
    1457592738726320825232114979368597902465568126723963659423258096484501066869825585939522443018423351
    0796993179521766048766401507852504354541123594001984288999281876521810626995316053067061881523522003
    9446124697444957872067638828228223820555769608015432377521852070443268314360460217371614518594665186
    9952154740029664053870191351601175125399460438802710652760886714912481747637009097610442338289695049
    6801243997626344084846104902281939310385537610143204390924013621494750986592575826551852206686816914
    5988889484169349244469708574839906632664085566491252770805407915140686288602030085400445338125182200
    2063397547475893808486356228939810160647615549271080607834624351762139830311024017952003263983433397
    9325817297051271109985048318611706085997631642523209939332794995557695539872037654361017789191715765
    6599323082848029769441991089468612433722665202552849770118102898580821961975957148550711190528190858
    2410664082430724017787955825880118721989339300003277860079253244161444607814477100684490666551972586
    7364607169807348254632405408226718752714812870966166171582635478228915736801870298534366725501137324
    4593111029319042926987995140240170010634106974485343317191440013210682446363969610731003605685843212
    1282606378325160050672661353532861791169959432322704653542881619435585392580022351152651422434511799
    3966398262964579806708204633097953356069054836450110915057056470360375217935176523945881167196827774
    0436108763500725695275730870930922714431806015813868216872170604504518240929797228142237641359833425
    0185608055932340589367063352082746023387590842471936253418176222883293397944075455383388633137255482
    7116783391013737783211388565178876316475549938868517619294097837951377838149833240105973581301003439
    3441004148321311058918081595102852846161443427143534957756418740954164369711286278855813047528852449
    4958831768540316011816224668962525549660293758918266838165767621163930724025152392508261837970551762
    7610622019300521741977837231454023939081580291893571776290105388036493464628629674194178443670811907
    1028132281146343907710384331103984977999346070867570880525757317370762603880769968951751974650829496
    8453830324800483399650375793485929695757773512067734963819420396885516746095026314067890097157419841
    7804472544561452030283363735918492135148312468758356731153223941032727293317426193188650817975319628
    6932375490062916947057447108724004490341805681235803358764858512378957781270946255673976276421193747
    2116494619510061811336484346905583482193782441484852655839250676812781125785862278279540687285811691
    3915164140239981466114036306561184707663508663094293233219760528816059803647978481226498614569200806
    0522277427531321840360511998911303285620669236571218889294462968805871936772077562156312511578040322
    3757679164778861235744538716995733464495079149650481930613886762821610985643458263253507994303476989
    1540307477832732632049181469452323498473804768987662425350144257267818310237162634930836208495418286
    8603976987722186681029757957617784874332374476271105048407508468879877688399536161930314610894307642
    5261714291077274060827086324445755046302735001171082270695750489509893238904380373174814639155448850
    3317307051380219631210063532692483843001435612052506942905112393375455785009520287347324860910257376
    9080861204288596936291906767897965220753340039197847556891445950069231915615864314192919303529164950
    7182669646397650686622773622040269449900733914028061398673986107199933847519686712184832722143408673
    1361044278616608016243714190899007921399996285048268248733421766963868372269220140770542179314021879
    4609369777026248393737377806540154250385824683798323952288804251762119428702119304076486404112030226
    2952610115697307669496757704034454450953434415881175947051492987448207616037304740321549995343636157
    0101616305140136822930565761437889590838721962604624222313867123462182223776925353850735026931459224
    9078107836777888420842602895401969440939018182501267626023360793893045540071892786389074854216667661
    3158566671453512077079917443643745378968300781005114106931145127004131008765667100642463420574053145
    1300562598902444054462011732238344686135722185776510112011681870235370687530859262058728509024338399
    7708961731323018133837095772621064051211505808971386102819486565224895830703429500406418340372157766
    6975877041181184835005262287523168640306119034890447014615343836716888576260793618030835062585832328
    9300305074054825129436992751555464496914801957584110610385368398993273817008252044590360253565064017
    9752939204460873689720716791033537021367662619942984041656660786015972842244221643376772083519478026
    6163246894697031848513616747698559768861557184980169331807335035159363393978215430178287145779088957
    5125505525769722137747009983085401163884655872811591735643803707984022331853211832025277430300072543
    8398937230414810826195283309588554443227610765212999024868293986194639040671004825427044663083217435
    8472284171320089106581822927721154807588164911541337373981181099222718368591828105531543721615618768
    8223401271024884128116010622239123710191839876069001927340031754500675046387504972610760792032689423
    0878726820359111830701504423191949181952826549696470989878165568140153030742354262409982282424799263
    0880010469587817626115972356916577748753580822731264186857832029885045237327866026998458780781911185
    3453712882555361326785115117178217812159237192943655090557552186200832407973163271255644808323514757
    7693727093645707009048781087954818557742386732187370335302885145613870111998597188360365428119248412
    1086109715971388184872704842772364207534762892557030690206288189987294197505845373905155726292354728
    1228827638031582173978322498696329692008530441913113271901076113892128778699116799346356335419633996
    5155448716689409816310297863610122512743800029238783982067023711507361910738112054516939657961673279
    8425391255605501998796281544686576221863020687695146576617392418823630178347967162520640993489940541
    0480580421093711318097587232018425177809295928134699762736054099762084902615104903977655545425045730
    6925087004339397620778878580604048031460940298484549319421077920601106580520457344188454535770635973
    9675883034501446946218668209128062555512643230613442597664575619727167528094245755361287869509148987
    1166053523094333066663034844411668932911343751824126779428444402367177101077400079414936854718600956
    6688319479397564967422224955389121257891890305207265146110108392566939410235355602135014616749341628
    6966749736482556022635303607913992522210267140099255100519797894139902027200892476931963408401083011
    5217878030010604255185689744755226819714858543424101974597120674747134085496456710225868909577713042
    7590288938211391193689010068753064700236098631179612228842003130788325055545841493604665078532204840
    4741249327214115158813610065061345803693104779621399416199760264197989792574006673305925665497188961
    0984672196924402339089356718215936445761913158633910364643576365668237124838680602154292219841531571
    5843089628534212319685091516256030614154793217304877268966059564715962454090523259759187361391334376
    2225761153005970328669116603361075500209057340062531650589932902995577899171691848611537715116596303
    5623215244533305377387289926305893668748008982327409566262922985671237903188526068603844495408140319
    9209547375519949191904744410703843451699550823885312028705123560463111272021936701528342768276308847
    3174446561176976218657979449277112206656483883239229387060790197180968340371470119530004475696853275
    9223750582413308798703594083053525868220820014447855915007742517386980339361427344874300237281999435
    1419138387114197360798867235551626932495357510571482085813966433565849081480375817927745195435764564
    0224296841309764388916984346364078057376992364755825920318623218529087106554523813396442540455753312
    8421268556450962680803773689464499088533347989856639037158463098753474203539705736460302078495936960
    0686696000855626475488208866690675592563363970029214159106548921217826367133486927917374978529496777
    7494442336593757670687583254085696122918590381709241299733363755904150771346545827113284825525306246
    0340382556580180168325439338413503398321308062548826241805100956546188569665657338493628082758767085
    2465507295680997934735876826211802794482162469676918981609918390485402996933566190170108158383949488
    5387490029847483308865683964809901463264474042555875473943223870177978447002930798148571036366120275
    5125260771998791229163633299336763512019511431652776786126942504547729072632425198065017662914572863
    1478108979532543741164861863916354679986101667998744227340949589783383799434118606276900335651141609
    7092664707358986563520559886428821529791192925719162930405587542133911567943036802770651795578737398
    5545278443608437883251008753461939696536700334403349890998383502361531418104404164832869314015784991
    4322888245795743255886916006302613208794073174642655256658981956110204881760084945099913452492848251
    2211879771275048013151287419548950099465363919813033240033014559994289145859613680448085479470815164
    3426194738112263238468358937056726669397150033655925564885543140886841152375762115070427998186517144
    7595053049444644704256998052610118654137811634649857913954091308475034129523991380306126325543194809
    25 33
    887365494202830000127770789940933
    255872907269262851388194273421768
    208252321149793685979024655681267
    660487664015078525043545411235940
    578720676388282282238205557696080
    640538701913516011751253994604388
    440848461049022819393103855376101
    492444697085748399066326640855664
    938084863562289398101606476155492
    711099850483186117060859976316425
    297694419910894686124337226652025
    240177879558258801187219893393000
    482546324054082267187527148128709
    429269879951402401700106341069744
    600506726613535328617911699594323
    798067082046330979533560690548364
    256952757308709309227144318060158
    405893670633520827460233875908424
    377832113885651788763164755499388
    110589180815951028528461614434271
    160118162246689625255496602937589
    217419778372314540239390815802918
    439077103843311039849779993460708
    833996503757934859296957577735120
    520302833637359184921351483124687
    '''
    inp = raw_inp.split() 
    r_grid, c_grid = int(inp[0]), int(inp[1])
    r_pat, c_pat = int(inp[r_grid+2]), int(inp[r_grid+3])

    G = []
    for i in range(r_grid):
        G.append(inp[i+2])
    
    P = []
    for i in range(r_pat):
        P.append(inp[i+r_grid+4])

    print(gridSearch(G,P))