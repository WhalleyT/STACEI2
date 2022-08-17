pdb_ranges = {"ATOM": range(0,4),
              "SERIAL": range(6, 11),
              "ATOM_NAME": range(12, 16),
              "ALT_LOC": range(16, 17),
              "RESIDUE_SEQID": range(17,20),
              "CHAIN": range(21, 22),
              "RESIDUE_NUM": range(22, 26),
              "INSERTION": range(26,27),
              "X_COORD": range(30, 38),
              "Y_COORD": range(38, 46),
              "Z_COORD": range(46, 54),
              "OCCUPANCY": range(54, 60),
              "TEMPERATURE": range(60, 66),
              "SEGMENT": range(72, 76),
              "ELEMENT": range(76, 78)}


mhc_ranges = {"class_1_MHCa1": range(50, 87),
              "class_1_MHCa2": range(140, 177),
              "class_2_MHCa1": range(46, 79),
              "class_2_MHCb1": range(54, 92)}

mhc_fastas = { "B2M" : "MSRSVALAVLALLSLSGLEAIQRTPKIQVYSRHPAENGKSNFLNCYVSGFHPSDIEVDLLKNGERIEKVEHSDLSFSKDWSFYLLYYTEFTPTEKDEYACRVNHVTLSQPKIVKWDRDM",
               ">HLA:HLA00001 A*01:01:01:01 365 bp" : "MAVMAPRTLLLLLSGALALTQTWAGSHSMRYFFTSVSRPGRGEPRFIAVGYVDDTQFVRFDSDAASQKMEPRAPWIEQEGPEYWDQETRNMKAHSQTDRANLGTLRGYYNQSEDGSHTIQIMYGCDVGPDGRFLRGYRQDAYDGKDYIALNEDLRSWTAADMAAQITKRKWEAVHAAEQRRVYLEGRCVDGLRRYLENGKETLQRTDPPKTHMTHHPISDHEATLRCWALGFYPAEITLTWQRDGEDQTQDTELVETRPAGDGTFQKWAAVVVPSGEEQRYTCHVQHEGLPKPLTLRWELSSQPTIPIVGIIAGLVLLGAVITGAVVAAVMWRRKSSDRKGGSYTQAASSDSAQGSDVSLTACKV",
               ">HLA:HLA00132 B*07:02:01:01 362 bp" : "MLVMAPRTVLLLLSAALALTETWAGSHSMRYFYTSVSRPGRGEPRFISVGYVDDTQFVRFDSDAASPREEPRAPWIEQEGPEYWDRNTQIYKAQAQTDRESLRNLRGYYNQSEAGSHTLQSMYGCDVGPDGRLLRGHDQYAYDGKDYIALNEDLRSWTAADTAAQITQRKWEAAREAEQRRAYLEGECVEWLRRYLENGKDKLERADPPKTHVTHHPISDHEATLRCWALGFYPAEITLTWQRDGEDQTQDTELVETRPAGDRTFQKWAAVVVPSGEEQRYTCHVQHEGLPKPLTLRWEPSSQSTVPIVGIVAGLAVLAVVVIGAVVAAVMCRRKSSGGKGGSYSQAACSDSAQGSDVSLTA",
               ">HLA:HLA00401 C*01:02:01:01 366 bp" : "MRVMAPRTLILLLSGALALTETWACSHSMKYFFTSVSRPGRGEPRFISVGYVDDTQFVRFDSDAASPRGEPRAPWVEQEGPEYWDRETQKYKRQAQTDRVSLRNLRGYYNQSEAGSHTLQWMCGCDLGPDGRLLRGYDQYAYDGKDYIALNEDLRSWTAADTAAQITQRKWEAAREAEQRRAYLEGTCVEWLRRYLENGKETLQRAEHPKTHVTHHPVSDHEATLRCWALGFYPAEITLTWQWDGEDQTQDTELVETRPAGDGTFQKWAAVMVPSGEEQRYTCHVQHEGLPEPLTLRWEPSSQPTIPIVGIVAGLAVLAVLAVLGAVVAVVMCRRKSSGGKGGSCSQAASSNSAQGSDESLIACKA",
               ">HLA:HLA00485 DMA*01:01:01:01 261 bp" : "MGHEQNQGAALLQMLPLLWLLPHSWAVPEAPTPMWPDDLQNHTFLHTVYCQDGSPSVGLSEAYDEDQLFFFDFSQNTRVPRLPEFADWAQEQGDAPAILFDKEFCEWMIQQIGPKLDGKIPVSRGFPIAEVFTLKPLEFGKPNTLVCFVSNLFPPMLTVNWQHHSVPVEGFGPTFVSAVDGLSFQAFSYLNFTPEPSDIFSCIVTHEIDRYTAIAYWVPRNALPSDLLENVLCGVAFGLGVLGIIVGIVLIIYFRKPCSGD",
               ">HLA:HLA00489 DMB*01:01:01:01 263 bp" : "MITFLPLLLGLSLGCTGAGGFVAHVESTCLLDDAGTPKDFTYCISFNKDLLTCWDPEENKMAPCEFGVLNSLANVLSQHLNQKDTLMQRLRNGLQNCATHTQPFWGSLTNRTRPPSVQVAKTTPFNTREPVMLACYVWGFYPAEVTITWRKNGKLVMPHSSAHKTAQPNGDWTYQTLSHLALTPSYGDTYTCVVEHIGAPEPILRDWTPGLSPMQTLKVSVSAVTLGLGLIIFSLGVISWRRAGHSSYTPLPGSNYSEGWHIS",
               ">HLA:HLA00494 DOA*01:01:01 250 bp" : "MALRAGLVLGFHTLMTLLSPQEAGATKADHMGSYGPAFYQSYGASGQFTHEFDEEQLFSVDLKKSEAVWRLPEFGDFARFDPQGGLAGIAAIKAHLDILVERSNRSRAINVPPRVTVLPKSRVELGQPNILICIVDNIFPPVINITWLRNGQTVTEGVAQTSFYSQPDHLFRKFHYLPFVPSAEDVYDCQVEHWGLDAPLLRHWELQVPIPPPDAMETLVCALGLAIGLVGFLVGTVLIIMGTYVSSVPR",
               ">HLA:HLA01098 DOB*01:01:01:01 273 bp" : "MGSGWVPWVVALLVNLTRLDSSMTQGTDSPEDFVIQAKADCYFTNGTEKVQFVVRFIFNLEEYVRFDSDVGMFVALTKLGQPDAEQWNSRLDLLERSRQAVDGVCRHNYRLGAPFTVGRKVQPEVTVYPERTPLLHQHNLLHCSVTGFYPGDIKIKWFLNGQEERAGVMSTGPIRNGDWTFQTVVMLEMTPELGHVYTCLVDHSSLLSPVSVEWRAQSEYSWRKMLSGIAAFLLGLIFLLVGIVIQLRAQKGYVRTQMSGNEVSRAVLLPQSC",
               ">HLA:HLA00499 DPA1*01:03:01:01 260 bp" : "MRPEDRMFHIRAVILRALSLAFLLSLRGAGAIKADHVSTYAAFVQTHRPTGEFMFEFDEDEMFYVDLDKKETVWHLEEFGQAFSFEAQGGLANIAILNNNLNTLIQRSNHTQATNDPPEVTVFPKEPVELGQPNTLICHIDKFFPPVLNVTWLCNGELVTEGVAESLFLPRTDYSFHKFHYLTFVPSAEDFYDCRVEHWGLDQPLLKHWEAQEPIQMPETTETVLCALGLVLGLVGIIVGTVLIIKSLRSGHDPRAQGTL",
               ">HLA:HLA16384 DPA2*01:01:01:01 104 bp" : "MSGVIKLPRVYVFCDWLPADHVSTYAEFVQTHRPSGEYMFEFDEEEQFYVNLDEKEMVWPLPEFIHTFDFGAQRGIAGIVMARKHLNTRINGPNRLGPQMPPPR",
               ">HLA:HLA00514 DPB1*01:01:01:01 258 bp" : "MMVLQVSAAPRTVALTALLMVLLTSVVQGRATPENYVYQGRQECYAFNGTQRFLERYIYNREEYARFDSDVGEFRAVTELGRPAAEYWNSQKDILEEKRAVPDRVCRHNYELDEAVTLQRRVQPKVNVSPSKKGPLQHHNLLVCHVTDFYPGSIQVRWFLNGQEETAGVVSTNLIRNGDWTFQILVMLEMTPQQGDVYICQVEHTSLDSPVTVEWKAQSDSAQSKTLTGAGGFVLGLIICGVGIFMHRRSKKVQRGSA",
               ">HLA:HLA14837 DPB2*01:01:01 145 bp" : "MMILQVSGGPWTVALTALLMVLLISVVQSRATPENSVYQERQECYAFNGTQRVVDGLIYNREEYVHFDSAVGEFLAVMELGRPIGEYFNSQKDFMERKRAEVDKVCRHKYELMEPLIRQRRVQPRVNIPPPRRSPGSTTTCLSTT",
               ">HLA:HLA00601 DQA1*01:01:01:01 255 bp" : "MILNKALLLGALALTTVMSPCGGEDIVADHVASCGVNLYQFYGPSGQYTHEFDGDEEFYVDLERKETAWRWPEFSKFGGFDPQGALRNMAVAKHNLNIMIKRYNSTAATNEVPEVTVFSKSPVTLGQPNTLICLVDNIFPPVVNITWLSNGQSVTEGVSETSFLSKSDHSFFKISYLTFLPSADEIYDCKVEHWGLDQPLLKHWEPEIPAPMSELTETVVCALGLSVGLVGIVVGTVFIIQGLRSVGASRHQGPL",
               ">HLA:HLA00622 DQB1*02:01:01 261 bp" : "MSWKKALRIPGGLRAATVTLMLSMLSTPVAEGRDSPEDFVYQFKGMCYFTNGTERVRLVSRSIYNREEIVRFDSDVGEFRAVTLLGLPAAEYWNSQKDILERKRAAVDRVCRHNYQLELRTTLQRRVEPTVTISPSRTEALNHHNLLVCSVTDFYPAQIKVRWFRNDQEETAGVVSTPLIRNGDWTFQILVMLEMTPQRGDVYTCHVEHPSLQSPITVEWRAQSESAQSKMLSGIGGFVLGLIFLGLGLIIHHRSQKGLLH",
               ">HLA:HLA00662 DRA*01:01:01:01 254 bp" : "MAISGVPVLGFFIIAVLMSAQESWAIKEEHVIIQAEFYLNPDQSGEFMFDFDGDEIFHVDMAKKETVWRLEEFGRFASFEAQGALANIAVDKANLEIMTKRSNYTPITNVPPEVTVLTNSPVELREPNVLICFIDKFTPPVVNVTWLRNGKPVTTGVSETVFLPREDHLFRKFHYLPFLPSTEDVYDCRVEHWGLDEPLLKHWEFDAPSPLPETTENVVCALGLTVGLVGIIIGTIFIIKGVRKSNAAERRGPL",
               ">HLA:HLA00664 DRB1*01:01:01 266 bp" : "MVCLKLPGGSCMTALTVTLMVLSSPLALAGDTRPRFLWQLKFECHFFNGTERVRLLERCIYNQEESVRFDSDVGEYRAVTELGRPDAEYWNSQKDLLEQRRAAVDTYCRHNYGVGESFTVQRRVEPKVTVYPSKTQPLQHHNLLVCSVSGFYPGSIEVRWFRNGQEEKAGVVSTGLIQNGDWTFQTLVMLETVPRSGEVYTCQVEHPSVTSPLTVEWRARSESAQSKMLSGVGGFVLGLLFLGAGLFIYFRNQKGHSGLQPTGFLS",
               ">HLA:HLA00934 E*01:01:01:01 358 bp" : "MVDGTLLLLLSEALALTQTWAGSHSLKYFHTSVSRPGRGEPRFISVGYVDDTQFVRFDNDAASPRMVPRAPWMEQEGSEYWDRETRSARDTAQIFRVNLRTLRGYYNQSEAGSHTLQWMHGCELGPDRRFLRGYEQFAYDGKDYLTLNEDLRSWTAVDTAAQISEQKSNDASEAEHQRAYLEDTCVEWLHKYLEKGKETLLHLEPPKTHVTHHPISDHEATLRCWALGFYPAEITLTWQQDGEGHTQDTELVETRPAGDGTFQKWAAVVVPSGEEQRYTCHVQHEGLPEPVTLRWKPASQPTIPIVGIIAGLVLLGSVVSGAVVAAVIWRKKSSGGKGGSYSKAEWSDSAQGSESHSL",
               ">HLA:HLA01096 F*01:01:01:01 346 bp" : "MAPRSLLLLLSGALALTDTWAGSHSLRYFSTAVSRPGRGEPRYIAVEYVDDTQFLRFDSDAAIPRMEPREPWVEQEGPQYWEWTTGYAKANAQTDRVALRNLLRRYNQSEAGSHTLQGMNGCDMGPDGRLLRGYHQHAYDGKDYISLNEDLRSWTAADTVAQITQRFYEAEEYAEEFRTYLEGECLELLRRYLENGKETLQRADPPKAHVAHHPISDHEATLRCWALGFYPAEITLTWQRDGEEQTQDTELVETRPAGDGTFQKWAAVVVPSGEEQRYTCHVQHEGLPQPLILRWEQSPQPTIPIVGIVAGLVVLGAVVTGAVVAAVMWRKKSSDRNRGSYSQAAV",
               ">HLA:HLA00939 G*01:01:01:01 338 bp" : "MVVMAPRTLFLLLSGALTLTETWAGSHSMRYFSAAVSRPGRGEPRFIAMGYVDDTQFVRFDSDSACPRMEPRAPWVEQEGPEYWEEETRNTKAHAQTDRMNLQTLRGYYNQSEASSHTLQWMIGCDLGSDGRLLRGYEQYAYDGKDYLALNEDLRSWTAADTAAQISKRKCEAANVAEQRRAYLEGTCVEWLHRYLENGKEMLQRADPPKTHVTHHPVFDYEATLRCWALGFYPAEIILTWQRDGEDQTQDVELVETRPAGDGTFQKWAAVVVPSGEEQRYTCHVQHEGLPEPLMLRWKQSSLPTIPIMGIVAGLVVLAAVVTGAAVAAVLWRKKSSD",
               ">HLA:HLA14067 HFE*001:01:01 348 bp" : "MGPRARPALLLLMLLQTAVLQGRLLRSHSLHYLFMGASEQDLGLSLFEALGYVDDQLFVFYDHESRRVEPRTPWVSSRISSQMWLQLSQSLKGWDHMFTVDFWTIMENHNHSKESHTLQVILGCEMQEDNSTEGYWKYGYDGQDHLEFCPDTLDWRAAEPRAWPTKLEWERHKIRARQNRAYLERDCPAQLQQLLELGRGVLDQQVPPLVKVTHHVTSSVTTLRCRALNYYPQNITMKWLKDKQPMDAKEFEPKDVLPNGDGTYQGWITLAVPPGEEQRYTCQVEHPGLDQPLIVIWEPSPSGTLVIGVISGIAVFVVILFIGILFIILRKRQGSRGAMGHYVLAERE",
               ">HLA:HLA01013 MICA*001 383 bp" : "MGLGPVFLLLAGIFPFAPPGAAAEPHSLRYNLTVLSWDGSVQSGFLTEVHLDGQPFLRCDRQKCRAKPQGQWAEDVLGNKTWDRETRDLTGNGKDLRMTLAHIKDQKEGLHSLQEIRVCEIHEDNSTRSSQHFYYDGELFLSQNLETKEWTMPQSSRAQTLAMNVRNFLKEDAMKTKTHYHAMHADCLQELRRYLKSGVVLRRTVPPMVNVTRSEASEGNITVTCRASGFYPWNITLSWRQDGVSLSHDTQQWGDVLPDGNGTYQTWVATRICQGEEQRFTCYMEHSGNHSTHPVPSGKVLVLQSHWQTFHVSAVAAAAIFVIIIFYVRCCKKKTSAAEGPELVSLQVLDQHPVGTSDHRDATQLGFQPLMSDLGSTGSTEGA",
               ">HLA:HLA02033 MICB*001 383 bp" : "MGLGRVLLFLAVAFPFAPPAAAAEPHSLRYNLMVLSQDESVQSGFLAEGHLDGQPFLRYDRQKRRAKPQGQWAEDVLGAKTWDTETEDLTENGQDLRRTLTHIKDQKGGLHSLQEIRVCEIHEDSSTRGSRHFYYDGELFLSQNLETQESTVPQSSRAQTLAMNVTNFWKEDAMKTKTHYRAMQADCLQKLQRYLKSGVAIRRTVPPMVNVTCSEVSEGNITVTCRASSFYPRNITLTWRQDGVSLSHNTQQWGDVLPDGNGTYQTWVATRIRQGEEQRFTCYMEHSGNHGTHPVPSGKVLVLQSQRTDFPYVSAAMPCFVIIIILCVPCCKKKTSAAEGPELVSLQVLDQHPVGTGDHRDAAQLGFQPLMSATGSTGSTEGA",
               ">HLA:HLA00953 TAP1*01:01:01:01 748 bp" : "MASSRCPAPRGCRCLPGASLAWLGTVLLLLADWVLLRTALPRIFSLLVPTALPLLRVWAVGLSRWAVLWLGACGVLRATVGSKSENAGAQGWLAALKPLAAALGLALPGLALFRELISWGAPGSADSTRLLHWGSHPTAFVVSYAAALPAAALWHKLGSLWVPGGQGGSGNPVRRLLGCLGSETRRLSLFLVLVVLSSLGEMAIPFFTGRLTDWILQDGSADTFTRNLTLMSILTIASAVLEFVGDGIYNNTMGHVHSHLQGEVFGAVLRQETEFFQQNQTGNIMSRVTEDTSTLSDSLSENLSLFLWYLVRGLCLLGIMLWGSVSLTMVTLITLPLLFLLPKKVGKWYQLLEVQVRESLAKSSQVAIEALSAMPTVRSFANEEGEAQKFREKLQEIKTLNQKEAVAYAVNSWTTSISGMLLKVGILYIGGQLVTSGAVSSGNLVTFVLYQMQFTQAVEVLLSIYPRVQKAVGSSEKIFEYLDRTPRCPPSGLLTPLHLEGLVQFQDVSFAYPNRPDVLVLQGLTFTLRPGEVTALVGPNGSGKSTVAALLQNLYQPTGGQLLLDGKPLPQYEHRYLHRQVAAVGQEPQVFGRSLQENIAYGLTQKPTMEEITAAAVKSGAHSFISGLPQGYDTEVDEAGSQLSGGQRQAVALARALIRKPCVLILDDATSALDANSQLQVEQLLYESPERYSRSVLLITQHLSLVEQADHILFLEGGAIREGGTHQQLMEKKGCYWAMVQAPADAPE",
               ">HLA:HLA00959 TAP2*01:01:01 686 bp" : "MRLPDLRPWTSLLLVDAALLWLLQGPLGTLLPQGLPGLWLEGTLRLGGLWGLLKLRGLLGFVGTLLLPLCLATPLTVSLRALVAGASRAPPARVASAPWSWLLVGYGAAGLSWSLWAVLSPPGAQEKEQDQVNNKVLMWRLLKLSRPDLPLLVAAFFFLVLAVLGETLIPHYSGRVIDILGGDFDPHAFASAIFFMCLFSFGSSLSAGCRGGCFTYTMSRINLRIREQLFSSLLRQDLGFFQETKTGELNSRLSSDTTLMSNWLPLNANVLLRSLVKVVGLYGFMLSISPRLTLLSLLHMPFTIAAEKVYNTRHQEVLREIQDAVARAGQVVREAVGGLQTVRSFGAEEHEVCRYKEALEQCRQLYWRRDLERALYLLVRRVLHLGVQMLMLSCGLQQMQDGELTQGSLLSFMIYQESVGSYVQTLVYIYGDMLSNVGAAEKVFSYMDRQPNLPSPGTLAPTTLQGVVKFQDVSFAYPNRPDRPVLKGLTFTLRPGEVTALVGPNGSGKSTVAALLQNLYQPTGGQVLLDEKPISQYEHCYLHSQVVSVGQEPVLFSGSVRNNIAYGLQSCEDDKVMAAAQAAHADDFIQEMEHGIYTDVGEKGSQLAAGQKQRLAIARALVRDPRVLILDEATSALDVQCEQALQDWNSRGDRTVLVIAHRLQTVQRAHQILVLQEGKLQKLAQL"}


cdr_ranges = {
    "CDR1a": range(27, 40),
    "CDR1b": range(27, 40),
    "CDR2a": range(56, 66),
    "CDR2b": range(56, 66),
    "CDR3a": range(104, 119),
    "CDR3b": range(104, 119),
}

crossing_angle_coords = {
    "corner1": "/corners//P/CYS`1/SG",
    "corner2": "/corners//P/CYS`2/SG",
    "corner3": "/corners//P/CYS`3/SG",
    "corner4": "/corners//P/CYS`4/SG",
    "TCRcentroida": "/corners//T/CYS`1/SG",
    "TCRcentroidb": "/corners//T/CYS`2/SG",
    "TCRcentroidaP": "/corners//U/ALA`1/N",
    "TCRcentroidbP": "/corners//U/LEU`2/CA",
    "MHCfita": "/corners//M/CYS`1/SG",
    "MHCfitb": "/corners//M/CYS`2/SG",
    "MHCafitP": "/corners//N/CYS`1/SG",
    "MHCbfitP": "/corners//N/CYS`2/SG",
    "MHCafitatTCR": "/corners//O/LEU`1/CA",
    "MHCbfitatTCR": "/corners//O/ALA`2/N",
    "MHCafitatTCRP": "/corners//Q/LEU`1/CA",
    "MHCbfitatTCRP": "/corners//Q/ALA`2/N",
    "planeAtTCRa": "/corners//V/VAL`1/O",
    "planeAtTCRb": "/corners//V/ALA`2/N"

}