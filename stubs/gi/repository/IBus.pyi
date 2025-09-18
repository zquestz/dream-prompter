import typing

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject

T = typing.TypeVar("T")

A: int = 65
AE: int = 198
Aacute: int = 193
Abelowdot: int = 16785056
Abreve: int = 451
Abreveacute: int = 16785070
Abrevebelowdot: int = 16785078
Abrevegrave: int = 16785072
Abrevehook: int = 16785074
Abrevetilde: int = 16785076
AccessX_Enable: int = 65136
AccessX_Feedback_Enable: int = 65137
Acircumflex: int = 194
Acircumflexacute: int = 16785060
Acircumflexbelowdot: int = 16785068
Acircumflexgrave: int = 16785062
Acircumflexhook: int = 16785064
Acircumflextilde: int = 16785066
Adiaeresis: int = 196
Agrave: int = 192
Ahook: int = 16785058
Alt_L: int = 65513
Alt_R: int = 65514
Amacron: int = 960
Aogonek: int = 417
Arabic_0: int = 16778848
Arabic_1: int = 16778849
Arabic_2: int = 16778850
Arabic_3: int = 16778851
Arabic_4: int = 16778852
Arabic_5: int = 16778853
Arabic_6: int = 16778854
Arabic_7: int = 16778855
Arabic_8: int = 16778856
Arabic_9: int = 16778857
Arabic_ain: int = 1497
Arabic_alef: int = 1479
Arabic_alefmaksura: int = 1513
Arabic_beh: int = 1480
Arabic_comma: int = 1452
Arabic_dad: int = 1494
Arabic_dal: int = 1487
Arabic_damma: int = 1519
Arabic_dammatan: int = 1516
Arabic_ddal: int = 16778888
Arabic_farsi_yeh: int = 16778956
Arabic_fatha: int = 1518
Arabic_fathatan: int = 1515
Arabic_feh: int = 1505
Arabic_fullstop: int = 16778964
Arabic_gaf: int = 16778927
Arabic_ghain: int = 1498
Arabic_ha: int = 1511
Arabic_hah: int = 1485
Arabic_hamza: int = 1473
Arabic_hamza_above: int = 16778836
Arabic_hamza_below: int = 16778837
Arabic_hamzaonalef: int = 1475
Arabic_hamzaonwaw: int = 1476
Arabic_hamzaonyeh: int = 1478
Arabic_hamzaunderalef: int = 1477
Arabic_heh: int = 1511
Arabic_heh_doachashmee: int = 16778942
Arabic_heh_goal: int = 16778945
Arabic_jeem: int = 1484
Arabic_jeh: int = 16778904
Arabic_kaf: int = 1507
Arabic_kasra: int = 1520
Arabic_kasratan: int = 1517
Arabic_keheh: int = 16778921
Arabic_khah: int = 1486
Arabic_lam: int = 1508
Arabic_madda_above: int = 16778835
Arabic_maddaonalef: int = 1474
Arabic_meem: int = 1509
Arabic_noon: int = 1510
Arabic_noon_ghunna: int = 16778938
Arabic_peh: int = 16778878
Arabic_percent: int = 16778858
Arabic_qaf: int = 1506
Arabic_question_mark: int = 1471
Arabic_ra: int = 1489
Arabic_rreh: int = 16778897
Arabic_sad: int = 1493
Arabic_seen: int = 1491
Arabic_semicolon: int = 1467
Arabic_shadda: int = 1521
Arabic_sheen: int = 1492
Arabic_sukun: int = 1522
Arabic_superscript_alef: int = 16778864
Arabic_switch: int = 65406
Arabic_tah: int = 1495
Arabic_tatweel: int = 1504
Arabic_tcheh: int = 16778886
Arabic_teh: int = 1482
Arabic_tehmarbuta: int = 1481
Arabic_thal: int = 1488
Arabic_theh: int = 1483
Arabic_tteh: int = 16778873
Arabic_veh: int = 16778916
Arabic_waw: int = 1512
Arabic_yeh: int = 1514
Arabic_yeh_baree: int = 16778962
Arabic_zah: int = 1496
Arabic_zain: int = 1490
Aring: int = 197
Armenian_AT: int = 16778552
Armenian_AYB: int = 16778545
Armenian_BEN: int = 16778546
Armenian_CHA: int = 16778569
Armenian_DA: int = 16778548
Armenian_DZA: int = 16778561
Armenian_E: int = 16778551
Armenian_FE: int = 16778582
Armenian_GHAT: int = 16778562
Armenian_GIM: int = 16778547
Armenian_HI: int = 16778565
Armenian_HO: int = 16778560
Armenian_INI: int = 16778555
Armenian_JE: int = 16778571
Armenian_KE: int = 16778580
Armenian_KEN: int = 16778559
Armenian_KHE: int = 16778557
Armenian_LYUN: int = 16778556
Armenian_MEN: int = 16778564
Armenian_NU: int = 16778566
Armenian_O: int = 16778581
Armenian_PE: int = 16778570
Armenian_PYUR: int = 16778579
Armenian_RA: int = 16778572
Armenian_RE: int = 16778576
Armenian_SE: int = 16778573
Armenian_SHA: int = 16778567
Armenian_TCHE: int = 16778563
Armenian_TO: int = 16778553
Armenian_TSA: int = 16778558
Armenian_TSO: int = 16778577
Armenian_TYUN: int = 16778575
Armenian_VEV: int = 16778574
Armenian_VO: int = 16778568
Armenian_VYUN: int = 16778578
Armenian_YECH: int = 16778549
Armenian_ZA: int = 16778550
Armenian_ZHE: int = 16778554
Armenian_accent: int = 16778587
Armenian_amanak: int = 16778588
Armenian_apostrophe: int = 16778586
Armenian_at: int = 16778600
Armenian_ayb: int = 16778593
Armenian_ben: int = 16778594
Armenian_but: int = 16778589
Armenian_cha: int = 16778617
Armenian_da: int = 16778596
Armenian_dza: int = 16778609
Armenian_e: int = 16778599
Armenian_exclam: int = 16778588
Armenian_fe: int = 16778630
Armenian_full_stop: int = 16778633
Armenian_ghat: int = 16778610
Armenian_gim: int = 16778595
Armenian_hi: int = 16778613
Armenian_ho: int = 16778608
Armenian_hyphen: int = 16778634
Armenian_ini: int = 16778603
Armenian_je: int = 16778619
Armenian_ke: int = 16778628
Armenian_ken: int = 16778607
Armenian_khe: int = 16778605
Armenian_ligature_ew: int = 16778631
Armenian_lyun: int = 16778604
Armenian_men: int = 16778612
Armenian_nu: int = 16778614
Armenian_o: int = 16778629
Armenian_paruyk: int = 16778590
Armenian_pe: int = 16778618
Armenian_pyur: int = 16778627
Armenian_question: int = 16778590
Armenian_ra: int = 16778620
Armenian_re: int = 16778624
Armenian_se: int = 16778621
Armenian_separation_mark: int = 16778589
Armenian_sha: int = 16778615
Armenian_shesht: int = 16778587
Armenian_tche: int = 16778611
Armenian_to: int = 16778601
Armenian_tsa: int = 16778606
Armenian_tso: int = 16778625
Armenian_tyun: int = 16778623
Armenian_verjaket: int = 16778633
Armenian_vev: int = 16778622
Armenian_vo: int = 16778616
Armenian_vyun: int = 16778626
Armenian_yech: int = 16778597
Armenian_yentamna: int = 16778634
Armenian_za: int = 16778598
Armenian_zhe: int = 16778602
Atilde: int = 195
AudibleBell_Enable: int = 65146
B: int = 66
Babovedot: int = 16784898
BackSpace: int = 65288
Begin: int = 65368
BounceKeys_Enable: int = 65140
Break: int = 65387
Byelorussian_SHORTU: int = 1726
Byelorussian_shortu: int = 1710
C: int = 67
Cabovedot: int = 709
Cacute: int = 454
Cancel: int = 65385
Caps_Lock: int = 65509
Ccaron: int = 456
Ccedilla: int = 199
Ccircumflex: int = 710
Clear: int = 65291
Codeinput: int = 65335
ColonSign: int = 16785569
Control_L: int = 65507
Control_R: int = 65508
CruzeiroSign: int = 16785570
Cyrillic_A: int = 1761
Cyrillic_BE: int = 1762
Cyrillic_CHE: int = 1790
Cyrillic_CHE_descender: int = 16778422
Cyrillic_CHE_vertstroke: int = 16778424
Cyrillic_DE: int = 1764
Cyrillic_DZHE: int = 1727
Cyrillic_E: int = 1788
Cyrillic_EF: int = 1766
Cyrillic_EL: int = 1772
Cyrillic_EM: int = 1773
Cyrillic_EN: int = 1774
Cyrillic_EN_descender: int = 16778402
Cyrillic_ER: int = 1778
Cyrillic_ES: int = 1779
Cyrillic_GHE: int = 1767
Cyrillic_GHE_bar: int = 16778386
Cyrillic_HA: int = 1768
Cyrillic_HARDSIGN: int = 1791
Cyrillic_HA_descender: int = 16778418
Cyrillic_I: int = 1769
Cyrillic_IE: int = 1765
Cyrillic_IO: int = 1715
Cyrillic_I_macron: int = 16778466
Cyrillic_JE: int = 1720
Cyrillic_KA: int = 1771
Cyrillic_KA_descender: int = 16778394
Cyrillic_KA_vertstroke: int = 16778396
Cyrillic_LJE: int = 1721
Cyrillic_NJE: int = 1722
Cyrillic_O: int = 1775
Cyrillic_O_bar: int = 16778472
Cyrillic_PE: int = 1776
Cyrillic_SCHWA: int = 16778456
Cyrillic_SHA: int = 1787
Cyrillic_SHCHA: int = 1789
Cyrillic_SHHA: int = 16778426
Cyrillic_SHORTI: int = 1770
Cyrillic_SOFTSIGN: int = 1784
Cyrillic_TE: int = 1780
Cyrillic_TSE: int = 1763
Cyrillic_U: int = 1781
Cyrillic_U_macron: int = 16778478
Cyrillic_U_straight: int = 16778414
Cyrillic_U_straight_bar: int = 16778416
Cyrillic_VE: int = 1783
Cyrillic_YA: int = 1777
Cyrillic_YERU: int = 1785
Cyrillic_YU: int = 1760
Cyrillic_ZE: int = 1786
Cyrillic_ZHE: int = 1782
Cyrillic_ZHE_descender: int = 16778390
Cyrillic_a: int = 1729
Cyrillic_be: int = 1730
Cyrillic_che: int = 1758
Cyrillic_che_descender: int = 16778423
Cyrillic_che_vertstroke: int = 16778425
Cyrillic_de: int = 1732
Cyrillic_dzhe: int = 1711
Cyrillic_e: int = 1756
Cyrillic_ef: int = 1734
Cyrillic_el: int = 1740
Cyrillic_em: int = 1741
Cyrillic_en: int = 1742
Cyrillic_en_descender: int = 16778403
Cyrillic_er: int = 1746
Cyrillic_es: int = 1747
Cyrillic_ghe: int = 1735
Cyrillic_ghe_bar: int = 16778387
Cyrillic_ha: int = 1736
Cyrillic_ha_descender: int = 16778419
Cyrillic_hardsign: int = 1759
Cyrillic_i: int = 1737
Cyrillic_i_macron: int = 16778467
Cyrillic_ie: int = 1733
Cyrillic_io: int = 1699
Cyrillic_je: int = 1704
Cyrillic_ka: int = 1739
Cyrillic_ka_descender: int = 16778395
Cyrillic_ka_vertstroke: int = 16778397
Cyrillic_lje: int = 1705
Cyrillic_nje: int = 1706
Cyrillic_o: int = 1743
Cyrillic_o_bar: int = 16778473
Cyrillic_pe: int = 1744
Cyrillic_schwa: int = 16778457
Cyrillic_sha: int = 1755
Cyrillic_shcha: int = 1757
Cyrillic_shha: int = 16778427
Cyrillic_shorti: int = 1738
Cyrillic_softsign: int = 1752
Cyrillic_te: int = 1748
Cyrillic_tse: int = 1731
Cyrillic_u: int = 1749
Cyrillic_u_macron: int = 16778479
Cyrillic_u_straight: int = 16778415
Cyrillic_u_straight_bar: int = 16778417
Cyrillic_ve: int = 1751
Cyrillic_ya: int = 1745
Cyrillic_yeru: int = 1753
Cyrillic_yu: int = 1728
Cyrillic_ze: int = 1754
Cyrillic_zhe: int = 1750
Cyrillic_zhe_descender: int = 16778391
D: int = 68
Dabovedot: int = 16784906
Dcaron: int = 463
Delete: int = 65535
DongSign: int = 16785579
Down: int = 65364
Dstroke: int = 464
E: int = 69
ENG: int = 957
ETH: int = 208
Eabovedot: int = 972
Eacute: int = 201
Ebelowdot: int = 16785080
Ecaron: int = 460
Ecircumflex: int = 202
Ecircumflexacute: int = 16785086
Ecircumflexbelowdot: int = 16785094
Ecircumflexgrave: int = 16785088
Ecircumflexhook: int = 16785090
Ecircumflextilde: int = 16785092
EcuSign: int = 16785568
Ediaeresis: int = 203
Egrave: int = 200
Ehook: int = 16785082
Eisu_Shift: int = 65327
Eisu_toggle: int = 65328
Emacron: int = 938
End: int = 65367
Eogonek: int = 458
Escape: int = 65307
Eth: int = 208
Etilde: int = 16785084
EuroSign: int = 8364
Execute: int = 65378
F: int = 70
F1: int = 65470
F10: int = 65479
F11: int = 65480
F12: int = 65481
F13: int = 65482
F14: int = 65483
F15: int = 65484
F16: int = 65485
F17: int = 65486
F18: int = 65487
F19: int = 65488
F2: int = 65471
F20: int = 65489
F21: int = 65490
F22: int = 65491
F23: int = 65492
F24: int = 65493
F25: int = 65494
F26: int = 65495
F27: int = 65496
F28: int = 65497
F29: int = 65498
F3: int = 65472
F30: int = 65499
F31: int = 65500
F32: int = 65501
F33: int = 65502
F34: int = 65503
F35: int = 65504
F4: int = 65473
F5: int = 65474
F6: int = 65475
F7: int = 65476
F8: int = 65477
F9: int = 65478
FFrancSign: int = 16785571
Fabovedot: int = 16784926
Farsi_0: int = 16778992
Farsi_1: int = 16778993
Farsi_2: int = 16778994
Farsi_3: int = 16778995
Farsi_4: int = 16778996
Farsi_5: int = 16778997
Farsi_6: int = 16778998
Farsi_7: int = 16778999
Farsi_8: int = 16779000
Farsi_9: int = 16779001
Farsi_yeh: int = 16778956
Find: int = 65384
First_Virtual_Screen: int = 65232
G: int = 71
Gabovedot: int = 725
Gbreve: int = 683
Gcaron: int = 16777702
Gcedilla: int = 939
Gcircumflex: int = 728
Georgian_an: int = 16781520
Georgian_ban: int = 16781521
Georgian_can: int = 16781546
Georgian_char: int = 16781549
Georgian_chin: int = 16781545
Georgian_cil: int = 16781548
Georgian_don: int = 16781523
Georgian_en: int = 16781524
Georgian_fi: int = 16781558
Georgian_gan: int = 16781522
Georgian_ghan: int = 16781542
Georgian_hae: int = 16781552
Georgian_har: int = 16781556
Georgian_he: int = 16781553
Georgian_hie: int = 16781554
Georgian_hoe: int = 16781557
Georgian_in: int = 16781528
Georgian_jhan: int = 16781551
Georgian_jil: int = 16781547
Georgian_kan: int = 16781529
Georgian_khar: int = 16781541
Georgian_las: int = 16781530
Georgian_man: int = 16781531
Georgian_nar: int = 16781532
Georgian_on: int = 16781533
Georgian_par: int = 16781534
Georgian_phar: int = 16781540
Georgian_qar: int = 16781543
Georgian_rae: int = 16781536
Georgian_san: int = 16781537
Georgian_shin: int = 16781544
Georgian_tan: int = 16781527
Georgian_tar: int = 16781538
Georgian_un: int = 16781539
Georgian_vin: int = 16781525
Georgian_we: int = 16781555
Georgian_xan: int = 16781550
Georgian_zen: int = 16781526
Georgian_zhar: int = 16781535
Greek_ALPHA: int = 1985
Greek_ALPHAaccent: int = 1953
Greek_BETA: int = 1986
Greek_CHI: int = 2007
Greek_DELTA: int = 1988
Greek_EPSILON: int = 1989
Greek_EPSILONaccent: int = 1954
Greek_ETA: int = 1991
Greek_ETAaccent: int = 1955
Greek_GAMMA: int = 1987
Greek_IOTA: int = 1993
Greek_IOTAaccent: int = 1956
Greek_IOTAdiaeresis: int = 1957
Greek_IOTAdieresis: int = 1957
Greek_KAPPA: int = 1994
Greek_LAMBDA: int = 1995
Greek_LAMDA: int = 1995
Greek_MU: int = 1996
Greek_NU: int = 1997
Greek_OMEGA: int = 2009
Greek_OMEGAaccent: int = 1963
Greek_OMICRON: int = 1999
Greek_OMICRONaccent: int = 1959
Greek_PHI: int = 2006
Greek_PI: int = 2000
Greek_PSI: int = 2008
Greek_RHO: int = 2001
Greek_SIGMA: int = 2002
Greek_TAU: int = 2004
Greek_THETA: int = 1992
Greek_UPSILON: int = 2005
Greek_UPSILONaccent: int = 1960
Greek_UPSILONdieresis: int = 1961
Greek_XI: int = 1998
Greek_ZETA: int = 1990
Greek_accentdieresis: int = 1966
Greek_alpha: int = 2017
Greek_alphaaccent: int = 1969
Greek_beta: int = 2018
Greek_chi: int = 2039
Greek_delta: int = 2020
Greek_epsilon: int = 2021
Greek_epsilonaccent: int = 1970
Greek_eta: int = 2023
Greek_etaaccent: int = 1971
Greek_finalsmallsigma: int = 2035
Greek_gamma: int = 2019
Greek_horizbar: int = 1967
Greek_iota: int = 2025
Greek_iotaaccent: int = 1972
Greek_iotaaccentdieresis: int = 1974
Greek_iotadieresis: int = 1973
Greek_kappa: int = 2026
Greek_lambda: int = 2027
Greek_lamda: int = 2027
Greek_mu: int = 2028
Greek_nu: int = 2029
Greek_omega: int = 2041
Greek_omegaaccent: int = 1979
Greek_omicron: int = 2031
Greek_omicronaccent: int = 1975
Greek_phi: int = 2038
Greek_pi: int = 2032
Greek_psi: int = 2040
Greek_rho: int = 2033
Greek_sigma: int = 2034
Greek_switch: int = 65406
Greek_tau: int = 2036
Greek_theta: int = 2024
Greek_upsilon: int = 2037
Greek_upsilonaccent: int = 1976
Greek_upsilonaccentdieresis: int = 1978
Greek_upsilondieresis: int = 1977
Greek_xi: int = 2030
Greek_zeta: int = 2022
H: int = 72
Hangul: int = 65329
Hangul_A: int = 3775
Hangul_AE: int = 3776
Hangul_AraeA: int = 3830
Hangul_AraeAE: int = 3831
Hangul_Banja: int = 65337
Hangul_Cieuc: int = 3770
Hangul_Codeinput: int = 65335
Hangul_Dikeud: int = 3751
Hangul_E: int = 3780
Hangul_EO: int = 3779
Hangul_EU: int = 3793
Hangul_End: int = 65331
Hangul_Hanja: int = 65332
Hangul_Hieuh: int = 3774
Hangul_I: int = 3795
Hangul_Ieung: int = 3767
Hangul_J_Cieuc: int = 3818
Hangul_J_Dikeud: int = 3802
Hangul_J_Hieuh: int = 3822
Hangul_J_Ieung: int = 3816
Hangul_J_Jieuj: int = 3817
Hangul_J_Khieuq: int = 3819
Hangul_J_Kiyeog: int = 3796
Hangul_J_KiyeogSios: int = 3798
Hangul_J_KkogjiDalrinIeung: int = 3833
Hangul_J_Mieum: int = 3811
Hangul_J_Nieun: int = 3799
Hangul_J_NieunHieuh: int = 3801
Hangul_J_NieunJieuj: int = 3800
Hangul_J_PanSios: int = 3832
Hangul_J_Phieuf: int = 3821
Hangul_J_Pieub: int = 3812
Hangul_J_PieubSios: int = 3813
Hangul_J_Rieul: int = 3803
Hangul_J_RieulHieuh: int = 3810
Hangul_J_RieulKiyeog: int = 3804
Hangul_J_RieulMieum: int = 3805
Hangul_J_RieulPhieuf: int = 3809
Hangul_J_RieulPieub: int = 3806
Hangul_J_RieulSios: int = 3807
Hangul_J_RieulTieut: int = 3808
Hangul_J_Sios: int = 3814
Hangul_J_SsangKiyeog: int = 3797
Hangul_J_SsangSios: int = 3815
Hangul_J_Tieut: int = 3820
Hangul_J_YeorinHieuh: int = 3834
Hangul_Jamo: int = 65333
Hangul_Jeonja: int = 65336
Hangul_Jieuj: int = 3768
Hangul_Khieuq: int = 3771
Hangul_Kiyeog: int = 3745
Hangul_KiyeogSios: int = 3747
Hangul_KkogjiDalrinIeung: int = 3827
Hangul_Mieum: int = 3761
Hangul_MultipleCandidate: int = 65341
Hangul_Nieun: int = 3748
Hangul_NieunHieuh: int = 3750
Hangul_NieunJieuj: int = 3749
Hangul_O: int = 3783
Hangul_OE: int = 3786
Hangul_PanSios: int = 3826
Hangul_Phieuf: int = 3773
Hangul_Pieub: int = 3762
Hangul_PieubSios: int = 3764
Hangul_PostHanja: int = 65339
Hangul_PreHanja: int = 65338
Hangul_PreviousCandidate: int = 65342
Hangul_Rieul: int = 3753
Hangul_RieulHieuh: int = 3760
Hangul_RieulKiyeog: int = 3754
Hangul_RieulMieum: int = 3755
Hangul_RieulPhieuf: int = 3759
Hangul_RieulPieub: int = 3756
Hangul_RieulSios: int = 3757
Hangul_RieulTieut: int = 3758
Hangul_RieulYeorinHieuh: int = 3823
Hangul_Romaja: int = 65334
Hangul_SingleCandidate: int = 65340
Hangul_Sios: int = 3765
Hangul_Special: int = 65343
Hangul_SsangDikeud: int = 3752
Hangul_SsangJieuj: int = 3769
Hangul_SsangKiyeog: int = 3746
Hangul_SsangPieub: int = 3763
Hangul_SsangSios: int = 3766
Hangul_Start: int = 65330
Hangul_SunkyeongeumMieum: int = 3824
Hangul_SunkyeongeumPhieuf: int = 3828
Hangul_SunkyeongeumPieub: int = 3825
Hangul_Tieut: int = 3772
Hangul_U: int = 3788
Hangul_WA: int = 3784
Hangul_WAE: int = 3785
Hangul_WE: int = 3790
Hangul_WEO: int = 3789
Hangul_WI: int = 3791
Hangul_YA: int = 3777
Hangul_YAE: int = 3778
Hangul_YE: int = 3782
Hangul_YEO: int = 3781
Hangul_YI: int = 3794
Hangul_YO: int = 3787
Hangul_YU: int = 3792
Hangul_YeorinHieuh: int = 3829
Hangul_switch: int = 65406
Hankaku: int = 65321
Hcircumflex: int = 678
Hebrew_switch: int = 65406
Help: int = 65386
Henkan: int = 65315
Henkan_Mode: int = 65315
Hiragana: int = 65317
Hiragana_Katakana: int = 65319
Home: int = 65360
Hstroke: int = 673
Hyper_L: int = 65517
Hyper_R: int = 65518
I: int = 73
INTERFACE_CONFIG: str = "org.freedesktop.IBus.Config"
INTERFACE_ENGINE: str = "org.freedesktop.IBus.Engine"
INTERFACE_FACTORY: str = "org.freedesktop.IBus.Factory"
INTERFACE_IBUS: str = "org.freedesktop.IBus"
INTERFACE_INPUT_CONTEXT: str = "org.freedesktop.IBus.InputContext"
INTERFACE_NOTIFICATIONS: str = "org.freedesktop.IBus.Notifications"
INTERFACE_PANEL: str = "org.freedesktop.IBus.Panel"
INTERFACE_PORTAL: str = "org.freedesktop.IBus.Portal"
ISO_Center_Object: int = 65075
ISO_Continuous_Underline: int = 65072
ISO_Discontinuous_Underline: int = 65073
ISO_Emphasize: int = 65074
ISO_Enter: int = 65076
ISO_Fast_Cursor_Down: int = 65071
ISO_Fast_Cursor_Left: int = 65068
ISO_Fast_Cursor_Right: int = 65069
ISO_Fast_Cursor_Up: int = 65070
ISO_First_Group: int = 65036
ISO_First_Group_Lock: int = 65037
ISO_Group_Latch: int = 65030
ISO_Group_Lock: int = 65031
ISO_Group_Shift: int = 65406
ISO_Last_Group: int = 65038
ISO_Last_Group_Lock: int = 65039
ISO_Left_Tab: int = 65056
ISO_Level2_Latch: int = 65026
ISO_Level3_Latch: int = 65028
ISO_Level3_Lock: int = 65029
ISO_Level3_Shift: int = 65027
ISO_Level5_Latch: int = 65042
ISO_Level5_Lock: int = 65043
ISO_Level5_Shift: int = 65041
ISO_Lock: int = 65025
ISO_Move_Line_Down: int = 65058
ISO_Move_Line_Up: int = 65057
ISO_Next_Group: int = 65032
ISO_Next_Group_Lock: int = 65033
ISO_Partial_Line_Down: int = 65060
ISO_Partial_Line_Up: int = 65059
ISO_Partial_Space_Left: int = 65061
ISO_Partial_Space_Right: int = 65062
ISO_Prev_Group: int = 65034
ISO_Prev_Group_Lock: int = 65035
ISO_Release_Both_Margins: int = 65067
ISO_Release_Margin_Left: int = 65065
ISO_Release_Margin_Right: int = 65066
ISO_Set_Margin_Left: int = 65063
ISO_Set_Margin_Right: int = 65064
Iabovedot: int = 681
Iacute: int = 205
Ibelowdot: int = 16785098
Ibreve: int = 16777516
Icircumflex: int = 206
Idiaeresis: int = 207
Igrave: int = 204
Ihook: int = 16785096
Imacron: int = 975
Insert: int = 65379
Iogonek: int = 967
Itilde: int = 933
J: int = 74
Jcircumflex: int = 684
K: int = 75
KEY_0: int = 48
KEY_1: int = 49
KEY_2: int = 50
KEY_3: int = 51
KEY_3270_AltCursor: int = 64784
KEY_3270_Attn: int = 64782
KEY_3270_BackTab: int = 64773
KEY_3270_ChangeScreen: int = 64793
KEY_3270_Copy: int = 64789
KEY_3270_CursorBlink: int = 64783
KEY_3270_CursorSelect: int = 64796
KEY_3270_DeleteWord: int = 64794
KEY_3270_Duplicate: int = 64769
KEY_3270_Enter: int = 64798
KEY_3270_EraseEOF: int = 64774
KEY_3270_EraseInput: int = 64775
KEY_3270_ExSelect: int = 64795
KEY_3270_FieldMark: int = 64770
KEY_3270_Ident: int = 64787
KEY_3270_Jump: int = 64786
KEY_3270_KeyClick: int = 64785
KEY_3270_Left2: int = 64772
KEY_3270_PA1: int = 64778
KEY_3270_PA2: int = 64779
KEY_3270_PA3: int = 64780
KEY_3270_Play: int = 64790
KEY_3270_PrintScreen: int = 64797
KEY_3270_Quit: int = 64777
KEY_3270_Record: int = 64792
KEY_3270_Reset: int = 64776
KEY_3270_Right2: int = 64771
KEY_3270_Rule: int = 64788
KEY_3270_Setup: int = 64791
KEY_3270_Test: int = 64781
KEY_4: int = 52
KEY_5: int = 53
KEY_6: int = 54
KEY_7: int = 55
KEY_8: int = 56
KEY_9: int = 57
KEY_A: int = 65
KEY_AE: int = 198
KEY_Aacute: int = 193
KEY_Abelowdot: int = 16785056
KEY_Abreve: int = 451
KEY_Abreveacute: int = 16785070
KEY_Abrevebelowdot: int = 16785078
KEY_Abrevegrave: int = 16785072
KEY_Abrevehook: int = 16785074
KEY_Abrevetilde: int = 16785076
KEY_AccessX_Enable: int = 65136
KEY_AccessX_Feedback_Enable: int = 65137
KEY_Acircumflex: int = 194
KEY_Acircumflexacute: int = 16785060
KEY_Acircumflexbelowdot: int = 16785068
KEY_Acircumflexgrave: int = 16785062
KEY_Acircumflexhook: int = 16785064
KEY_Acircumflextilde: int = 16785066
KEY_AddFavorite: int = 269025081
KEY_Adiaeresis: int = 196
KEY_Agrave: int = 192
KEY_Ahook: int = 16785058
KEY_Alt_L: int = 65513
KEY_Alt_R: int = 65514
KEY_Amacron: int = 960
KEY_Aogonek: int = 417
KEY_ApplicationLeft: int = 269025104
KEY_ApplicationRight: int = 269025105
KEY_Arabic_0: int = 16778848
KEY_Arabic_1: int = 16778849
KEY_Arabic_2: int = 16778850
KEY_Arabic_3: int = 16778851
KEY_Arabic_4: int = 16778852
KEY_Arabic_5: int = 16778853
KEY_Arabic_6: int = 16778854
KEY_Arabic_7: int = 16778855
KEY_Arabic_8: int = 16778856
KEY_Arabic_9: int = 16778857
KEY_Arabic_ain: int = 1497
KEY_Arabic_alef: int = 1479
KEY_Arabic_alefmaksura: int = 1513
KEY_Arabic_beh: int = 1480
KEY_Arabic_comma: int = 1452
KEY_Arabic_dad: int = 1494
KEY_Arabic_dal: int = 1487
KEY_Arabic_damma: int = 1519
KEY_Arabic_dammatan: int = 1516
KEY_Arabic_ddal: int = 16778888
KEY_Arabic_farsi_yeh: int = 16778956
KEY_Arabic_fatha: int = 1518
KEY_Arabic_fathatan: int = 1515
KEY_Arabic_feh: int = 1505
KEY_Arabic_fullstop: int = 16778964
KEY_Arabic_gaf: int = 16778927
KEY_Arabic_ghain: int = 1498
KEY_Arabic_ha: int = 1511
KEY_Arabic_hah: int = 1485
KEY_Arabic_hamza: int = 1473
KEY_Arabic_hamza_above: int = 16778836
KEY_Arabic_hamza_below: int = 16778837
KEY_Arabic_hamzaonalef: int = 1475
KEY_Arabic_hamzaonwaw: int = 1476
KEY_Arabic_hamzaonyeh: int = 1478
KEY_Arabic_hamzaunderalef: int = 1477
KEY_Arabic_heh: int = 1511
KEY_Arabic_heh_doachashmee: int = 16778942
KEY_Arabic_heh_goal: int = 16778945
KEY_Arabic_jeem: int = 1484
KEY_Arabic_jeh: int = 16778904
KEY_Arabic_kaf: int = 1507
KEY_Arabic_kasra: int = 1520
KEY_Arabic_kasratan: int = 1517
KEY_Arabic_keheh: int = 16778921
KEY_Arabic_khah: int = 1486
KEY_Arabic_lam: int = 1508
KEY_Arabic_madda_above: int = 16778835
KEY_Arabic_maddaonalef: int = 1474
KEY_Arabic_meem: int = 1509
KEY_Arabic_noon: int = 1510
KEY_Arabic_noon_ghunna: int = 16778938
KEY_Arabic_peh: int = 16778878
KEY_Arabic_percent: int = 16778858
KEY_Arabic_qaf: int = 1506
KEY_Arabic_question_mark: int = 1471
KEY_Arabic_ra: int = 1489
KEY_Arabic_rreh: int = 16778897
KEY_Arabic_sad: int = 1493
KEY_Arabic_seen: int = 1491
KEY_Arabic_semicolon: int = 1467
KEY_Arabic_shadda: int = 1521
KEY_Arabic_sheen: int = 1492
KEY_Arabic_sukun: int = 1522
KEY_Arabic_superscript_alef: int = 16778864
KEY_Arabic_switch: int = 65406
KEY_Arabic_tah: int = 1495
KEY_Arabic_tatweel: int = 1504
KEY_Arabic_tcheh: int = 16778886
KEY_Arabic_teh: int = 1482
KEY_Arabic_tehmarbuta: int = 1481
KEY_Arabic_thal: int = 1488
KEY_Arabic_theh: int = 1483
KEY_Arabic_tteh: int = 16778873
KEY_Arabic_veh: int = 16778916
KEY_Arabic_waw: int = 1512
KEY_Arabic_yeh: int = 1514
KEY_Arabic_yeh_baree: int = 16778962
KEY_Arabic_zah: int = 1496
KEY_Arabic_zain: int = 1490
KEY_Aring: int = 197
KEY_Armenian_AT: int = 16778552
KEY_Armenian_AYB: int = 16778545
KEY_Armenian_BEN: int = 16778546
KEY_Armenian_CHA: int = 16778569
KEY_Armenian_DA: int = 16778548
KEY_Armenian_DZA: int = 16778561
KEY_Armenian_E: int = 16778551
KEY_Armenian_FE: int = 16778582
KEY_Armenian_GHAT: int = 16778562
KEY_Armenian_GIM: int = 16778547
KEY_Armenian_HI: int = 16778565
KEY_Armenian_HO: int = 16778560
KEY_Armenian_INI: int = 16778555
KEY_Armenian_JE: int = 16778571
KEY_Armenian_KE: int = 16778580
KEY_Armenian_KEN: int = 16778559
KEY_Armenian_KHE: int = 16778557
KEY_Armenian_LYUN: int = 16778556
KEY_Armenian_MEN: int = 16778564
KEY_Armenian_NU: int = 16778566
KEY_Armenian_O: int = 16778581
KEY_Armenian_PE: int = 16778570
KEY_Armenian_PYUR: int = 16778579
KEY_Armenian_RA: int = 16778572
KEY_Armenian_RE: int = 16778576
KEY_Armenian_SE: int = 16778573
KEY_Armenian_SHA: int = 16778567
KEY_Armenian_TCHE: int = 16778563
KEY_Armenian_TO: int = 16778553
KEY_Armenian_TSA: int = 16778558
KEY_Armenian_TSO: int = 16778577
KEY_Armenian_TYUN: int = 16778575
KEY_Armenian_VEV: int = 16778574
KEY_Armenian_VO: int = 16778568
KEY_Armenian_VYUN: int = 16778578
KEY_Armenian_YECH: int = 16778549
KEY_Armenian_ZA: int = 16778550
KEY_Armenian_ZHE: int = 16778554
KEY_Armenian_accent: int = 16778587
KEY_Armenian_amanak: int = 16778588
KEY_Armenian_apostrophe: int = 16778586
KEY_Armenian_at: int = 16778600
KEY_Armenian_ayb: int = 16778593
KEY_Armenian_ben: int = 16778594
KEY_Armenian_but: int = 16778589
KEY_Armenian_cha: int = 16778617
KEY_Armenian_da: int = 16778596
KEY_Armenian_dza: int = 16778609
KEY_Armenian_e: int = 16778599
KEY_Armenian_exclam: int = 16778588
KEY_Armenian_fe: int = 16778630
KEY_Armenian_full_stop: int = 16778633
KEY_Armenian_ghat: int = 16778610
KEY_Armenian_gim: int = 16778595
KEY_Armenian_hi: int = 16778613
KEY_Armenian_ho: int = 16778608
KEY_Armenian_hyphen: int = 16778634
KEY_Armenian_ini: int = 16778603
KEY_Armenian_je: int = 16778619
KEY_Armenian_ke: int = 16778628
KEY_Armenian_ken: int = 16778607
KEY_Armenian_khe: int = 16778605
KEY_Armenian_ligature_ew: int = 16778631
KEY_Armenian_lyun: int = 16778604
KEY_Armenian_men: int = 16778612
KEY_Armenian_nu: int = 16778614
KEY_Armenian_o: int = 16778629
KEY_Armenian_paruyk: int = 16778590
KEY_Armenian_pe: int = 16778618
KEY_Armenian_pyur: int = 16778627
KEY_Armenian_question: int = 16778590
KEY_Armenian_ra: int = 16778620
KEY_Armenian_re: int = 16778624
KEY_Armenian_se: int = 16778621
KEY_Armenian_separation_mark: int = 16778589
KEY_Armenian_sha: int = 16778615
KEY_Armenian_shesht: int = 16778587
KEY_Armenian_tche: int = 16778611
KEY_Armenian_to: int = 16778601
KEY_Armenian_tsa: int = 16778606
KEY_Armenian_tso: int = 16778625
KEY_Armenian_tyun: int = 16778623
KEY_Armenian_verjaket: int = 16778633
KEY_Armenian_vev: int = 16778622
KEY_Armenian_vo: int = 16778616
KEY_Armenian_vyun: int = 16778626
KEY_Armenian_yech: int = 16778597
KEY_Armenian_yentamna: int = 16778634
KEY_Armenian_za: int = 16778598
KEY_Armenian_zhe: int = 16778602
KEY_Atilde: int = 195
KEY_AudibleBell_Enable: int = 65146
KEY_AudioCycleTrack: int = 269025179
KEY_AudioForward: int = 269025175
KEY_AudioLowerVolume: int = 269025041
KEY_AudioMedia: int = 269025074
KEY_AudioMicMute: int = 269025202
KEY_AudioMute: int = 269025042
KEY_AudioNext: int = 269025047
KEY_AudioPause: int = 269025073
KEY_AudioPlay: int = 269025044
KEY_AudioPreset: int = 269025206
KEY_AudioPrev: int = 269025046
KEY_AudioRaiseVolume: int = 269025043
KEY_AudioRandomPlay: int = 269025177
KEY_AudioRecord: int = 269025052
KEY_AudioRepeat: int = 269025176
KEY_AudioRewind: int = 269025086
KEY_AudioStop: int = 269025045
KEY_Away: int = 269025165
KEY_B: int = 66
KEY_Babovedot: int = 16784898
KEY_Back: int = 269025062
KEY_BackForward: int = 269025087
KEY_BackSpace: int = 65288
KEY_Battery: int = 269025171
KEY_Begin: int = 65368
KEY_Blue: int = 269025190
KEY_Bluetooth: int = 269025172
KEY_Book: int = 269025106
KEY_BounceKeys_Enable: int = 65140
KEY_Break: int = 65387
KEY_BrightnessAdjust: int = 269025083
KEY_Byelorussian_SHORTU: int = 1726
KEY_Byelorussian_shortu: int = 1710
KEY_C: int = 67
KEY_CD: int = 269025107
KEY_CH: int = 65186
KEY_C_H: int = 65189
KEY_C_h: int = 65188
KEY_Cabovedot: int = 709
KEY_Cacute: int = 454
KEY_Calculator: int = 269025053
KEY_Calendar: int = 269025056
KEY_Cancel: int = 65385
KEY_Caps_Lock: int = 65509
KEY_Ccaron: int = 456
KEY_Ccedilla: int = 199
KEY_Ccircumflex: int = 710
KEY_Ch: int = 65185
KEY_Clear: int = 65291
KEY_ClearGrab: int = 269024801
KEY_Close: int = 269025110
KEY_Codeinput: int = 65335
KEY_ColonSign: int = 16785569
KEY_Community: int = 269025085
KEY_ContrastAdjust: int = 269025058
KEY_Control_L: int = 65507
KEY_Control_R: int = 65508
KEY_Copy: int = 269025111
KEY_CruzeiroSign: int = 16785570
KEY_Cut: int = 269025112
KEY_CycleAngle: int = 269025180
KEY_Cyrillic_A: int = 1761
KEY_Cyrillic_BE: int = 1762
KEY_Cyrillic_CHE: int = 1790
KEY_Cyrillic_CHE_descender: int = 16778422
KEY_Cyrillic_CHE_vertstroke: int = 16778424
KEY_Cyrillic_DE: int = 1764
KEY_Cyrillic_DZHE: int = 1727
KEY_Cyrillic_E: int = 1788
KEY_Cyrillic_EF: int = 1766
KEY_Cyrillic_EL: int = 1772
KEY_Cyrillic_EM: int = 1773
KEY_Cyrillic_EN: int = 1774
KEY_Cyrillic_EN_descender: int = 16778402
KEY_Cyrillic_ER: int = 1778
KEY_Cyrillic_ES: int = 1779
KEY_Cyrillic_GHE: int = 1767
KEY_Cyrillic_GHE_bar: int = 16778386
KEY_Cyrillic_HA: int = 1768
KEY_Cyrillic_HARDSIGN: int = 1791
KEY_Cyrillic_HA_descender: int = 16778418
KEY_Cyrillic_I: int = 1769
KEY_Cyrillic_IE: int = 1765
KEY_Cyrillic_IO: int = 1715
KEY_Cyrillic_I_macron: int = 16778466
KEY_Cyrillic_JE: int = 1720
KEY_Cyrillic_KA: int = 1771
KEY_Cyrillic_KA_descender: int = 16778394
KEY_Cyrillic_KA_vertstroke: int = 16778396
KEY_Cyrillic_LJE: int = 1721
KEY_Cyrillic_NJE: int = 1722
KEY_Cyrillic_O: int = 1775
KEY_Cyrillic_O_bar: int = 16778472
KEY_Cyrillic_PE: int = 1776
KEY_Cyrillic_SCHWA: int = 16778456
KEY_Cyrillic_SHA: int = 1787
KEY_Cyrillic_SHCHA: int = 1789
KEY_Cyrillic_SHHA: int = 16778426
KEY_Cyrillic_SHORTI: int = 1770
KEY_Cyrillic_SOFTSIGN: int = 1784
KEY_Cyrillic_TE: int = 1780
KEY_Cyrillic_TSE: int = 1763
KEY_Cyrillic_U: int = 1781
KEY_Cyrillic_U_macron: int = 16778478
KEY_Cyrillic_U_straight: int = 16778414
KEY_Cyrillic_U_straight_bar: int = 16778416
KEY_Cyrillic_VE: int = 1783
KEY_Cyrillic_YA: int = 1777
KEY_Cyrillic_YERU: int = 1785
KEY_Cyrillic_YU: int = 1760
KEY_Cyrillic_ZE: int = 1786
KEY_Cyrillic_ZHE: int = 1782
KEY_Cyrillic_ZHE_descender: int = 16778390
KEY_Cyrillic_a: int = 1729
KEY_Cyrillic_be: int = 1730
KEY_Cyrillic_che: int = 1758
KEY_Cyrillic_che_descender: int = 16778423
KEY_Cyrillic_che_vertstroke: int = 16778425
KEY_Cyrillic_de: int = 1732
KEY_Cyrillic_dzhe: int = 1711
KEY_Cyrillic_e: int = 1756
KEY_Cyrillic_ef: int = 1734
KEY_Cyrillic_el: int = 1740
KEY_Cyrillic_em: int = 1741
KEY_Cyrillic_en: int = 1742
KEY_Cyrillic_en_descender: int = 16778403
KEY_Cyrillic_er: int = 1746
KEY_Cyrillic_es: int = 1747
KEY_Cyrillic_ghe: int = 1735
KEY_Cyrillic_ghe_bar: int = 16778387
KEY_Cyrillic_ha: int = 1736
KEY_Cyrillic_ha_descender: int = 16778419
KEY_Cyrillic_hardsign: int = 1759
KEY_Cyrillic_i: int = 1737
KEY_Cyrillic_i_macron: int = 16778467
KEY_Cyrillic_ie: int = 1733
KEY_Cyrillic_io: int = 1699
KEY_Cyrillic_je: int = 1704
KEY_Cyrillic_ka: int = 1739
KEY_Cyrillic_ka_descender: int = 16778395
KEY_Cyrillic_ka_vertstroke: int = 16778397
KEY_Cyrillic_lje: int = 1705
KEY_Cyrillic_nje: int = 1706
KEY_Cyrillic_o: int = 1743
KEY_Cyrillic_o_bar: int = 16778473
KEY_Cyrillic_pe: int = 1744
KEY_Cyrillic_schwa: int = 16778457
KEY_Cyrillic_sha: int = 1755
KEY_Cyrillic_shcha: int = 1757
KEY_Cyrillic_shha: int = 16778427
KEY_Cyrillic_shorti: int = 1738
KEY_Cyrillic_softsign: int = 1752
KEY_Cyrillic_te: int = 1748
KEY_Cyrillic_tse: int = 1731
KEY_Cyrillic_u: int = 1749
KEY_Cyrillic_u_macron: int = 16778479
KEY_Cyrillic_u_straight: int = 16778415
KEY_Cyrillic_u_straight_bar: int = 16778417
KEY_Cyrillic_ve: int = 1751
KEY_Cyrillic_ya: int = 1745
KEY_Cyrillic_yeru: int = 1753
KEY_Cyrillic_yu: int = 1728
KEY_Cyrillic_ze: int = 1754
KEY_Cyrillic_zhe: int = 1750
KEY_Cyrillic_zhe_descender: int = 16778391
KEY_D: int = 68
KEY_DOS: int = 269025114
KEY_Dabovedot: int = 16784906
KEY_Dcaron: int = 463
KEY_Delete: int = 65535
KEY_Display: int = 269025113
KEY_Documents: int = 269025115
KEY_DongSign: int = 16785579
KEY_Down: int = 65364
KEY_Dstroke: int = 464
KEY_E: int = 69
KEY_ENG: int = 957
KEY_ETH: int = 208
KEY_EZH: int = 16777655
KEY_Eabovedot: int = 972
KEY_Eacute: int = 201
KEY_Ebelowdot: int = 16785080
KEY_Ecaron: int = 460
KEY_Ecircumflex: int = 202
KEY_Ecircumflexacute: int = 16785086
KEY_Ecircumflexbelowdot: int = 16785094
KEY_Ecircumflexgrave: int = 16785088
KEY_Ecircumflexhook: int = 16785090
KEY_Ecircumflextilde: int = 16785092
KEY_EcuSign: int = 16785568
KEY_Ediaeresis: int = 203
KEY_Egrave: int = 200
KEY_Ehook: int = 16785082
KEY_Eisu_Shift: int = 65327
KEY_Eisu_toggle: int = 65328
KEY_Eject: int = 269025068
KEY_Emacron: int = 938
KEY_End: int = 65367
KEY_Eogonek: int = 458
KEY_Escape: int = 65307
KEY_Eth: int = 208
KEY_Etilde: int = 16785084
KEY_EuroSign: int = 8364
KEY_Excel: int = 269025116
KEY_Execute: int = 65378
KEY_Explorer: int = 269025117
KEY_F: int = 70
KEY_F1: int = 65470
KEY_F10: int = 65479
KEY_F11: int = 65480
KEY_F12: int = 65481
KEY_F13: int = 65482
KEY_F14: int = 65483
KEY_F15: int = 65484
KEY_F16: int = 65485
KEY_F17: int = 65486
KEY_F18: int = 65487
KEY_F19: int = 65488
KEY_F2: int = 65471
KEY_F20: int = 65489
KEY_F21: int = 65490
KEY_F22: int = 65491
KEY_F23: int = 65492
KEY_F24: int = 65493
KEY_F25: int = 65494
KEY_F26: int = 65495
KEY_F27: int = 65496
KEY_F28: int = 65497
KEY_F29: int = 65498
KEY_F3: int = 65472
KEY_F30: int = 65499
KEY_F31: int = 65500
KEY_F32: int = 65501
KEY_F33: int = 65502
KEY_F34: int = 65503
KEY_F35: int = 65504
KEY_F4: int = 65473
KEY_F5: int = 65474
KEY_F6: int = 65475
KEY_F7: int = 65476
KEY_F8: int = 65477
KEY_F9: int = 65478
KEY_FFrancSign: int = 16785571
KEY_Fabovedot: int = 16784926
KEY_Farsi_0: int = 16778992
KEY_Farsi_1: int = 16778993
KEY_Farsi_2: int = 16778994
KEY_Farsi_3: int = 16778995
KEY_Farsi_4: int = 16778996
KEY_Farsi_5: int = 16778997
KEY_Farsi_6: int = 16778998
KEY_Farsi_7: int = 16778999
KEY_Farsi_8: int = 16779000
KEY_Farsi_9: int = 16779001
KEY_Farsi_yeh: int = 16778956
KEY_Favorites: int = 269025072
KEY_Finance: int = 269025084
KEY_Find: int = 65384
KEY_First_Virtual_Screen: int = 65232
KEY_Forward: int = 269025063
KEY_FrameBack: int = 269025181
KEY_FrameForward: int = 269025182
KEY_G: int = 71
KEY_Gabovedot: int = 725
KEY_Game: int = 269025118
KEY_Gbreve: int = 683
KEY_Gcaron: int = 16777702
KEY_Gcedilla: int = 939
KEY_Gcircumflex: int = 728
KEY_Georgian_an: int = 16781520
KEY_Georgian_ban: int = 16781521
KEY_Georgian_can: int = 16781546
KEY_Georgian_char: int = 16781549
KEY_Georgian_chin: int = 16781545
KEY_Georgian_cil: int = 16781548
KEY_Georgian_don: int = 16781523
KEY_Georgian_en: int = 16781524
KEY_Georgian_fi: int = 16781558
KEY_Georgian_gan: int = 16781522
KEY_Georgian_ghan: int = 16781542
KEY_Georgian_hae: int = 16781552
KEY_Georgian_har: int = 16781556
KEY_Georgian_he: int = 16781553
KEY_Georgian_hie: int = 16781554
KEY_Georgian_hoe: int = 16781557
KEY_Georgian_in: int = 16781528
KEY_Georgian_jhan: int = 16781551
KEY_Georgian_jil: int = 16781547
KEY_Georgian_kan: int = 16781529
KEY_Georgian_khar: int = 16781541
KEY_Georgian_las: int = 16781530
KEY_Georgian_man: int = 16781531
KEY_Georgian_nar: int = 16781532
KEY_Georgian_on: int = 16781533
KEY_Georgian_par: int = 16781534
KEY_Georgian_phar: int = 16781540
KEY_Georgian_qar: int = 16781543
KEY_Georgian_rae: int = 16781536
KEY_Georgian_san: int = 16781537
KEY_Georgian_shin: int = 16781544
KEY_Georgian_tan: int = 16781527
KEY_Georgian_tar: int = 16781538
KEY_Georgian_un: int = 16781539
KEY_Georgian_vin: int = 16781525
KEY_Georgian_we: int = 16781555
KEY_Georgian_xan: int = 16781550
KEY_Georgian_zen: int = 16781526
KEY_Georgian_zhar: int = 16781535
KEY_Go: int = 269025119
KEY_Greek_ALPHA: int = 1985
KEY_Greek_ALPHAaccent: int = 1953
KEY_Greek_BETA: int = 1986
KEY_Greek_CHI: int = 2007
KEY_Greek_DELTA: int = 1988
KEY_Greek_EPSILON: int = 1989
KEY_Greek_EPSILONaccent: int = 1954
KEY_Greek_ETA: int = 1991
KEY_Greek_ETAaccent: int = 1955
KEY_Greek_GAMMA: int = 1987
KEY_Greek_IOTA: int = 1993
KEY_Greek_IOTAaccent: int = 1956
KEY_Greek_IOTAdiaeresis: int = 1957
KEY_Greek_IOTAdieresis: int = 1957
KEY_Greek_KAPPA: int = 1994
KEY_Greek_LAMBDA: int = 1995
KEY_Greek_LAMDA: int = 1995
KEY_Greek_MU: int = 1996
KEY_Greek_NU: int = 1997
KEY_Greek_OMEGA: int = 2009
KEY_Greek_OMEGAaccent: int = 1963
KEY_Greek_OMICRON: int = 1999
KEY_Greek_OMICRONaccent: int = 1959
KEY_Greek_PHI: int = 2006
KEY_Greek_PI: int = 2000
KEY_Greek_PSI: int = 2008
KEY_Greek_RHO: int = 2001
KEY_Greek_SIGMA: int = 2002
KEY_Greek_TAU: int = 2004
KEY_Greek_THETA: int = 1992
KEY_Greek_UPSILON: int = 2005
KEY_Greek_UPSILONaccent: int = 1960
KEY_Greek_UPSILONdieresis: int = 1961
KEY_Greek_XI: int = 1998
KEY_Greek_ZETA: int = 1990
KEY_Greek_accentdieresis: int = 1966
KEY_Greek_alpha: int = 2017
KEY_Greek_alphaaccent: int = 1969
KEY_Greek_beta: int = 2018
KEY_Greek_chi: int = 2039
KEY_Greek_delta: int = 2020
KEY_Greek_epsilon: int = 2021
KEY_Greek_epsilonaccent: int = 1970
KEY_Greek_eta: int = 2023
KEY_Greek_etaaccent: int = 1971
KEY_Greek_finalsmallsigma: int = 2035
KEY_Greek_gamma: int = 2019
KEY_Greek_horizbar: int = 1967
KEY_Greek_iota: int = 2025
KEY_Greek_iotaaccent: int = 1972
KEY_Greek_iotaaccentdieresis: int = 1974
KEY_Greek_iotadieresis: int = 1973
KEY_Greek_kappa: int = 2026
KEY_Greek_lambda: int = 2027
KEY_Greek_lamda: int = 2027
KEY_Greek_mu: int = 2028
KEY_Greek_nu: int = 2029
KEY_Greek_omega: int = 2041
KEY_Greek_omegaaccent: int = 1979
KEY_Greek_omicron: int = 2031
KEY_Greek_omicronaccent: int = 1975
KEY_Greek_phi: int = 2038
KEY_Greek_pi: int = 2032
KEY_Greek_psi: int = 2040
KEY_Greek_rho: int = 2033
KEY_Greek_sigma: int = 2034
KEY_Greek_switch: int = 65406
KEY_Greek_tau: int = 2036
KEY_Greek_theta: int = 2024
KEY_Greek_upsilon: int = 2037
KEY_Greek_upsilonaccent: int = 1976
KEY_Greek_upsilonaccentdieresis: int = 1978
KEY_Greek_upsilondieresis: int = 1977
KEY_Greek_xi: int = 2030
KEY_Greek_zeta: int = 2022
KEY_Green: int = 269025188
KEY_H: int = 72
KEY_Hangul: int = 65329
KEY_Hangul_A: int = 3775
KEY_Hangul_AE: int = 3776
KEY_Hangul_AraeA: int = 3830
KEY_Hangul_AraeAE: int = 3831
KEY_Hangul_Banja: int = 65337
KEY_Hangul_Cieuc: int = 3770
KEY_Hangul_Codeinput: int = 65335
KEY_Hangul_Dikeud: int = 3751
KEY_Hangul_E: int = 3780
KEY_Hangul_EO: int = 3779
KEY_Hangul_EU: int = 3793
KEY_Hangul_End: int = 65331
KEY_Hangul_Hanja: int = 65332
KEY_Hangul_Hieuh: int = 3774
KEY_Hangul_I: int = 3795
KEY_Hangul_Ieung: int = 3767
KEY_Hangul_J_Cieuc: int = 3818
KEY_Hangul_J_Dikeud: int = 3802
KEY_Hangul_J_Hieuh: int = 3822
KEY_Hangul_J_Ieung: int = 3816
KEY_Hangul_J_Jieuj: int = 3817
KEY_Hangul_J_Khieuq: int = 3819
KEY_Hangul_J_Kiyeog: int = 3796
KEY_Hangul_J_KiyeogSios: int = 3798
KEY_Hangul_J_KkogjiDalrinIeung: int = 3833
KEY_Hangul_J_Mieum: int = 3811
KEY_Hangul_J_Nieun: int = 3799
KEY_Hangul_J_NieunHieuh: int = 3801
KEY_Hangul_J_NieunJieuj: int = 3800
KEY_Hangul_J_PanSios: int = 3832
KEY_Hangul_J_Phieuf: int = 3821
KEY_Hangul_J_Pieub: int = 3812
KEY_Hangul_J_PieubSios: int = 3813
KEY_Hangul_J_Rieul: int = 3803
KEY_Hangul_J_RieulHieuh: int = 3810
KEY_Hangul_J_RieulKiyeog: int = 3804
KEY_Hangul_J_RieulMieum: int = 3805
KEY_Hangul_J_RieulPhieuf: int = 3809
KEY_Hangul_J_RieulPieub: int = 3806
KEY_Hangul_J_RieulSios: int = 3807
KEY_Hangul_J_RieulTieut: int = 3808
KEY_Hangul_J_Sios: int = 3814
KEY_Hangul_J_SsangKiyeog: int = 3797
KEY_Hangul_J_SsangSios: int = 3815
KEY_Hangul_J_Tieut: int = 3820
KEY_Hangul_J_YeorinHieuh: int = 3834
KEY_Hangul_Jamo: int = 65333
KEY_Hangul_Jeonja: int = 65336
KEY_Hangul_Jieuj: int = 3768
KEY_Hangul_Khieuq: int = 3771
KEY_Hangul_Kiyeog: int = 3745
KEY_Hangul_KiyeogSios: int = 3747
KEY_Hangul_KkogjiDalrinIeung: int = 3827
KEY_Hangul_Mieum: int = 3761
KEY_Hangul_MultipleCandidate: int = 65341
KEY_Hangul_Nieun: int = 3748
KEY_Hangul_NieunHieuh: int = 3750
KEY_Hangul_NieunJieuj: int = 3749
KEY_Hangul_O: int = 3783
KEY_Hangul_OE: int = 3786
KEY_Hangul_PanSios: int = 3826
KEY_Hangul_Phieuf: int = 3773
KEY_Hangul_Pieub: int = 3762
KEY_Hangul_PieubSios: int = 3764
KEY_Hangul_PostHanja: int = 65339
KEY_Hangul_PreHanja: int = 65338
KEY_Hangul_PreviousCandidate: int = 65342
KEY_Hangul_Rieul: int = 3753
KEY_Hangul_RieulHieuh: int = 3760
KEY_Hangul_RieulKiyeog: int = 3754
KEY_Hangul_RieulMieum: int = 3755
KEY_Hangul_RieulPhieuf: int = 3759
KEY_Hangul_RieulPieub: int = 3756
KEY_Hangul_RieulSios: int = 3757
KEY_Hangul_RieulTieut: int = 3758
KEY_Hangul_RieulYeorinHieuh: int = 3823
KEY_Hangul_Romaja: int = 65334
KEY_Hangul_SingleCandidate: int = 65340
KEY_Hangul_Sios: int = 3765
KEY_Hangul_Special: int = 65343
KEY_Hangul_SsangDikeud: int = 3752
KEY_Hangul_SsangJieuj: int = 3769
KEY_Hangul_SsangKiyeog: int = 3746
KEY_Hangul_SsangPieub: int = 3763
KEY_Hangul_SsangSios: int = 3766
KEY_Hangul_Start: int = 65330
KEY_Hangul_SunkyeongeumMieum: int = 3824
KEY_Hangul_SunkyeongeumPhieuf: int = 3828
KEY_Hangul_SunkyeongeumPieub: int = 3825
KEY_Hangul_Tieut: int = 3772
KEY_Hangul_U: int = 3788
KEY_Hangul_WA: int = 3784
KEY_Hangul_WAE: int = 3785
KEY_Hangul_WE: int = 3790
KEY_Hangul_WEO: int = 3789
KEY_Hangul_WI: int = 3791
KEY_Hangul_YA: int = 3777
KEY_Hangul_YAE: int = 3778
KEY_Hangul_YE: int = 3782
KEY_Hangul_YEO: int = 3781
KEY_Hangul_YI: int = 3794
KEY_Hangul_YO: int = 3787
KEY_Hangul_YU: int = 3792
KEY_Hangul_YeorinHieuh: int = 3829
KEY_Hangul_switch: int = 65406
KEY_Hankaku: int = 65321
KEY_Hcircumflex: int = 678
KEY_Hebrew_switch: int = 65406
KEY_Help: int = 65386
KEY_Henkan: int = 65315
KEY_Henkan_Mode: int = 65315
KEY_Hibernate: int = 269025192
KEY_Hiragana: int = 65317
KEY_Hiragana_Katakana: int = 65319
KEY_History: int = 269025079
KEY_Home: int = 65360
KEY_HomePage: int = 269025048
KEY_HotLinks: int = 269025082
KEY_Hstroke: int = 673
KEY_Hyper_L: int = 65517
KEY_Hyper_R: int = 65518
KEY_I: int = 73
KEY_ISO_Center_Object: int = 65075
KEY_ISO_Continuous_Underline: int = 65072
KEY_ISO_Discontinuous_Underline: int = 65073
KEY_ISO_Emphasize: int = 65074
KEY_ISO_Enter: int = 65076
KEY_ISO_Fast_Cursor_Down: int = 65071
KEY_ISO_Fast_Cursor_Left: int = 65068
KEY_ISO_Fast_Cursor_Right: int = 65069
KEY_ISO_Fast_Cursor_Up: int = 65070
KEY_ISO_First_Group: int = 65036
KEY_ISO_First_Group_Lock: int = 65037
KEY_ISO_Group_Latch: int = 65030
KEY_ISO_Group_Lock: int = 65031
KEY_ISO_Group_Shift: int = 65406
KEY_ISO_Last_Group: int = 65038
KEY_ISO_Last_Group_Lock: int = 65039
KEY_ISO_Left_Tab: int = 65056
KEY_ISO_Level2_Latch: int = 65026
KEY_ISO_Level3_Latch: int = 65028
KEY_ISO_Level3_Lock: int = 65029
KEY_ISO_Level3_Shift: int = 65027
KEY_ISO_Level5_Latch: int = 65042
KEY_ISO_Level5_Lock: int = 65043
KEY_ISO_Level5_Shift: int = 65041
KEY_ISO_Lock: int = 65025
KEY_ISO_Move_Line_Down: int = 65058
KEY_ISO_Move_Line_Up: int = 65057
KEY_ISO_Next_Group: int = 65032
KEY_ISO_Next_Group_Lock: int = 65033
KEY_ISO_Partial_Line_Down: int = 65060
KEY_ISO_Partial_Line_Up: int = 65059
KEY_ISO_Partial_Space_Left: int = 65061
KEY_ISO_Partial_Space_Right: int = 65062
KEY_ISO_Prev_Group: int = 65034
KEY_ISO_Prev_Group_Lock: int = 65035
KEY_ISO_Release_Both_Margins: int = 65067
KEY_ISO_Release_Margin_Left: int = 65065
KEY_ISO_Release_Margin_Right: int = 65066
KEY_ISO_Set_Margin_Left: int = 65063
KEY_ISO_Set_Margin_Right: int = 65064
KEY_Iabovedot: int = 681
KEY_Iacute: int = 205
KEY_Ibelowdot: int = 16785098
KEY_Ibreve: int = 16777516
KEY_Icircumflex: int = 206
KEY_Idiaeresis: int = 207
KEY_Igrave: int = 204
KEY_Ihook: int = 16785096
KEY_Imacron: int = 975
KEY_Insert: int = 65379
KEY_Iogonek: int = 967
KEY_Itilde: int = 933
KEY_J: int = 74
KEY_Jcircumflex: int = 684
KEY_K: int = 75
KEY_KP_0: int = 65456
KEY_KP_1: int = 65457
KEY_KP_2: int = 65458
KEY_KP_3: int = 65459
KEY_KP_4: int = 65460
KEY_KP_5: int = 65461
KEY_KP_6: int = 65462
KEY_KP_7: int = 65463
KEY_KP_8: int = 65464
KEY_KP_9: int = 65465
KEY_KP_Add: int = 65451
KEY_KP_Begin: int = 65437
KEY_KP_Decimal: int = 65454
KEY_KP_Delete: int = 65439
KEY_KP_Divide: int = 65455
KEY_KP_Down: int = 65433
KEY_KP_End: int = 65436
KEY_KP_Enter: int = 65421
KEY_KP_Equal: int = 65469
KEY_KP_F1: int = 65425
KEY_KP_F2: int = 65426
KEY_KP_F3: int = 65427
KEY_KP_F4: int = 65428
KEY_KP_Home: int = 65429
KEY_KP_Insert: int = 65438
KEY_KP_Left: int = 65430
KEY_KP_Multiply: int = 65450
KEY_KP_Next: int = 65435
KEY_KP_Page_Down: int = 65435
KEY_KP_Page_Up: int = 65434
KEY_KP_Prior: int = 65434
KEY_KP_Right: int = 65432
KEY_KP_Separator: int = 65452
KEY_KP_Space: int = 65408
KEY_KP_Subtract: int = 65453
KEY_KP_Tab: int = 65417
KEY_KP_Up: int = 65431
KEY_Kana_Lock: int = 65325
KEY_Kana_Shift: int = 65326
KEY_Kanji: int = 65313
KEY_Kanji_Bangou: int = 65335
KEY_Katakana: int = 65318
KEY_KbdBrightnessDown: int = 269025030
KEY_KbdBrightnessUp: int = 269025029
KEY_KbdLightOnOff: int = 269025028
KEY_Kcedilla: int = 979
KEY_Keyboard: int = 269025203
KEY_Korean_Won: int = 3839
KEY_L: int = 76
KEY_L1: int = 65480
KEY_L10: int = 65489
KEY_L2: int = 65481
KEY_L3: int = 65482
KEY_L4: int = 65483
KEY_L5: int = 65484
KEY_L6: int = 65485
KEY_L7: int = 65486
KEY_L8: int = 65487
KEY_L9: int = 65488
KEY_Lacute: int = 453
KEY_Last_Virtual_Screen: int = 65236
KEY_Launch0: int = 269025088
KEY_Launch1: int = 269025089
KEY_Launch2: int = 269025090
KEY_Launch3: int = 269025091
KEY_Launch4: int = 269025092
KEY_Launch5: int = 269025093
KEY_Launch6: int = 269025094
KEY_Launch7: int = 269025095
KEY_Launch8: int = 269025096
KEY_Launch9: int = 269025097
KEY_LaunchA: int = 269025098
KEY_LaunchB: int = 269025099
KEY_LaunchC: int = 269025100
KEY_LaunchD: int = 269025101
KEY_LaunchE: int = 269025102
KEY_LaunchF: int = 269025103
KEY_Lbelowdot: int = 16784950
KEY_Lcaron: int = 421
KEY_Lcedilla: int = 934
KEY_Left: int = 65361
KEY_LightBulb: int = 269025077
KEY_Linefeed: int = 65290
KEY_LiraSign: int = 16785572
KEY_LogGrabInfo: int = 269024805
KEY_LogOff: int = 269025121
KEY_LogWindowTree: int = 269024804
KEY_Lstroke: int = 419
KEY_M: int = 77
KEY_Mabovedot: int = 16784960
KEY_Macedonia_DSE: int = 1717
KEY_Macedonia_GJE: int = 1714
KEY_Macedonia_KJE: int = 1724
KEY_Macedonia_dse: int = 1701
KEY_Macedonia_gje: int = 1698
KEY_Macedonia_kje: int = 1708
KEY_Mae_Koho: int = 65342
KEY_Mail: int = 269025049
KEY_MailForward: int = 269025168
KEY_Market: int = 269025122
KEY_Massyo: int = 65324
KEY_Meeting: int = 269025123
KEY_Memo: int = 269025054
KEY_Menu: int = 65383
KEY_MenuKB: int = 269025125
KEY_MenuPB: int = 269025126
KEY_Messenger: int = 269025166
KEY_Meta_L: int = 65511
KEY_Meta_R: int = 65512
KEY_MillSign: int = 16785573
KEY_ModeLock: int = 269025025
KEY_Mode_switch: int = 65406
KEY_MonBrightnessDown: int = 269025027
KEY_MonBrightnessUp: int = 269025026
KEY_MouseKeys_Accel_Enable: int = 65143
KEY_MouseKeys_Enable: int = 65142
KEY_Muhenkan: int = 65314
KEY_Multi_key: int = 65312
KEY_MultipleCandidate: int = 65341
KEY_Music: int = 269025170
KEY_MyComputer: int = 269025075
KEY_MySites: int = 269025127
KEY_N: int = 78
KEY_Nacute: int = 465
KEY_NairaSign: int = 16785574
KEY_Ncaron: int = 466
KEY_Ncedilla: int = 977
KEY_New: int = 269025128
KEY_NewSheqelSign: int = 16785578
KEY_News: int = 269025129
KEY_Next: int = 65366
KEY_Next_VMode: int = 269024802
KEY_Next_Virtual_Screen: int = 65234
KEY_Ntilde: int = 209
KEY_Num_Lock: int = 65407
KEY_O: int = 79
KEY_OE: int = 5052
KEY_Oacute: int = 211
KEY_Obarred: int = 16777631
KEY_Obelowdot: int = 16785100
KEY_Ocaron: int = 16777681
KEY_Ocircumflex: int = 212
KEY_Ocircumflexacute: int = 16785104
KEY_Ocircumflexbelowdot: int = 16785112
KEY_Ocircumflexgrave: int = 16785106
KEY_Ocircumflexhook: int = 16785108
KEY_Ocircumflextilde: int = 16785110
KEY_Odiaeresis: int = 214
KEY_Odoubleacute: int = 469
KEY_OfficeHome: int = 269025130
KEY_Ograve: int = 210
KEY_Ohook: int = 16785102
KEY_Ohorn: int = 16777632
KEY_Ohornacute: int = 16785114
KEY_Ohornbelowdot: int = 16785122
KEY_Ohorngrave: int = 16785116
KEY_Ohornhook: int = 16785118
KEY_Ohorntilde: int = 16785120
KEY_Omacron: int = 978
KEY_Ooblique: int = 216
KEY_Open: int = 269025131
KEY_OpenURL: int = 269025080
KEY_Option: int = 269025132
KEY_Oslash: int = 216
KEY_Otilde: int = 213
KEY_Overlay1_Enable: int = 65144
KEY_Overlay2_Enable: int = 65145
KEY_P: int = 80
KEY_Pabovedot: int = 16784982
KEY_Page_Down: int = 65366
KEY_Page_Up: int = 65365
KEY_Paste: int = 269025133
KEY_Pause: int = 65299
KEY_PesetaSign: int = 16785575
KEY_Phone: int = 269025134
KEY_Pictures: int = 269025169
KEY_Pointer_Accelerate: int = 65274
KEY_Pointer_Button1: int = 65257
KEY_Pointer_Button2: int = 65258
KEY_Pointer_Button3: int = 65259
KEY_Pointer_Button4: int = 65260
KEY_Pointer_Button5: int = 65261
KEY_Pointer_Button_Dflt: int = 65256
KEY_Pointer_DblClick1: int = 65263
KEY_Pointer_DblClick2: int = 65264
KEY_Pointer_DblClick3: int = 65265
KEY_Pointer_DblClick4: int = 65266
KEY_Pointer_DblClick5: int = 65267
KEY_Pointer_DblClick_Dflt: int = 65262
KEY_Pointer_DfltBtnNext: int = 65275
KEY_Pointer_DfltBtnPrev: int = 65276
KEY_Pointer_Down: int = 65251
KEY_Pointer_DownLeft: int = 65254
KEY_Pointer_DownRight: int = 65255
KEY_Pointer_Drag1: int = 65269
KEY_Pointer_Drag2: int = 65270
KEY_Pointer_Drag3: int = 65271
KEY_Pointer_Drag4: int = 65272
KEY_Pointer_Drag5: int = 65277
KEY_Pointer_Drag_Dflt: int = 65268
KEY_Pointer_EnableKeys: int = 65273
KEY_Pointer_Left: int = 65248
KEY_Pointer_Right: int = 65249
KEY_Pointer_Up: int = 65250
KEY_Pointer_UpLeft: int = 65252
KEY_Pointer_UpRight: int = 65253
KEY_PowerDown: int = 269025057
KEY_PowerOff: int = 269025066
KEY_Prev_VMode: int = 269024803
KEY_Prev_Virtual_Screen: int = 65233
KEY_PreviousCandidate: int = 65342
KEY_Print: int = 65377
KEY_Prior: int = 65365
KEY_Q: int = 81
KEY_R: int = 82
KEY_R1: int = 65490
KEY_R10: int = 65499
KEY_R11: int = 65500
KEY_R12: int = 65501
KEY_R13: int = 65502
KEY_R14: int = 65503
KEY_R15: int = 65504
KEY_R2: int = 65491
KEY_R3: int = 65492
KEY_R4: int = 65493
KEY_R5: int = 65494
KEY_R6: int = 65495
KEY_R7: int = 65496
KEY_R8: int = 65497
KEY_R9: int = 65498
KEY_RFKill: int = 269025205
KEY_Racute: int = 448
KEY_Rcaron: int = 472
KEY_Rcedilla: int = 931
KEY_Red: int = 269025187
KEY_Redo: int = 65382
KEY_Refresh: int = 269025065
KEY_Reload: int = 269025139
KEY_RepeatKeys_Enable: int = 65138
KEY_Reply: int = 269025138
KEY_Return: int = 65293
KEY_Right: int = 65363
KEY_RockerDown: int = 269025060
KEY_RockerEnter: int = 269025061
KEY_RockerUp: int = 269025059
KEY_Romaji: int = 65316
KEY_RotateWindows: int = 269025140
KEY_RotationKB: int = 269025142
KEY_RotationPB: int = 269025141
KEY_RupeeSign: int = 16785576
KEY_S: int = 83
KEY_SCHWA: int = 16777615
KEY_Sabovedot: int = 16784992
KEY_Sacute: int = 422
KEY_Save: int = 269025143
KEY_Scaron: int = 425
KEY_Scedilla: int = 426
KEY_Scircumflex: int = 734
KEY_ScreenSaver: int = 269025069
KEY_ScrollClick: int = 269025146
KEY_ScrollDown: int = 269025145
KEY_ScrollUp: int = 269025144
KEY_Scroll_Lock: int = 65300
KEY_Search: int = 269025051
KEY_Select: int = 65376
KEY_SelectButton: int = 269025184
KEY_Send: int = 269025147
KEY_Serbian_DJE: int = 1713
KEY_Serbian_DZE: int = 1727
KEY_Serbian_JE: int = 1720
KEY_Serbian_LJE: int = 1721
KEY_Serbian_NJE: int = 1722
KEY_Serbian_TSHE: int = 1723
KEY_Serbian_dje: int = 1697
KEY_Serbian_dze: int = 1711
KEY_Serbian_je: int = 1704
KEY_Serbian_lje: int = 1705
KEY_Serbian_nje: int = 1706
KEY_Serbian_tshe: int = 1707
KEY_Shift_L: int = 65505
KEY_Shift_Lock: int = 65510
KEY_Shift_R: int = 65506
KEY_Shop: int = 269025078
KEY_SingleCandidate: int = 65340
KEY_Sinh_a: int = 16780677
KEY_Sinh_aa: int = 16780678
KEY_Sinh_aa2: int = 16780751
KEY_Sinh_ae: int = 16780679
KEY_Sinh_ae2: int = 16780752
KEY_Sinh_aee: int = 16780680
KEY_Sinh_aee2: int = 16780753
KEY_Sinh_ai: int = 16780691
KEY_Sinh_ai2: int = 16780763
KEY_Sinh_al: int = 16780746
KEY_Sinh_au: int = 16780694
KEY_Sinh_au2: int = 16780766
KEY_Sinh_ba: int = 16780726
KEY_Sinh_bha: int = 16780727
KEY_Sinh_ca: int = 16780704
KEY_Sinh_cha: int = 16780705
KEY_Sinh_dda: int = 16780713
KEY_Sinh_ddha: int = 16780714
KEY_Sinh_dha: int = 16780719
KEY_Sinh_dhha: int = 16780720
KEY_Sinh_e: int = 16780689
KEY_Sinh_e2: int = 16780761
KEY_Sinh_ee: int = 16780690
KEY_Sinh_ee2: int = 16780762
KEY_Sinh_fa: int = 16780742
KEY_Sinh_ga: int = 16780700
KEY_Sinh_gha: int = 16780701
KEY_Sinh_h2: int = 16780675
KEY_Sinh_ha: int = 16780740
KEY_Sinh_i: int = 16780681
KEY_Sinh_i2: int = 16780754
KEY_Sinh_ii: int = 16780682
KEY_Sinh_ii2: int = 16780755
KEY_Sinh_ja: int = 16780706
KEY_Sinh_jha: int = 16780707
KEY_Sinh_jnya: int = 16780709
KEY_Sinh_ka: int = 16780698
KEY_Sinh_kha: int = 16780699
KEY_Sinh_kunddaliya: int = 16780788
KEY_Sinh_la: int = 16780733
KEY_Sinh_lla: int = 16780741
KEY_Sinh_lu: int = 16780687
KEY_Sinh_lu2: int = 16780767
KEY_Sinh_luu: int = 16780688
KEY_Sinh_luu2: int = 16780787
KEY_Sinh_ma: int = 16780728
KEY_Sinh_mba: int = 16780729
KEY_Sinh_na: int = 16780721
KEY_Sinh_ndda: int = 16780716
KEY_Sinh_ndha: int = 16780723
KEY_Sinh_ng: int = 16780674
KEY_Sinh_ng2: int = 16780702
KEY_Sinh_nga: int = 16780703
KEY_Sinh_nja: int = 16780710
KEY_Sinh_nna: int = 16780715
KEY_Sinh_nya: int = 16780708
KEY_Sinh_o: int = 16780692
KEY_Sinh_o2: int = 16780764
KEY_Sinh_oo: int = 16780693
KEY_Sinh_oo2: int = 16780765
KEY_Sinh_pa: int = 16780724
KEY_Sinh_pha: int = 16780725
KEY_Sinh_ra: int = 16780731
KEY_Sinh_ri: int = 16780685
KEY_Sinh_rii: int = 16780686
KEY_Sinh_ru2: int = 16780760
KEY_Sinh_ruu2: int = 16780786
KEY_Sinh_sa: int = 16780739
KEY_Sinh_sha: int = 16780737
KEY_Sinh_ssha: int = 16780738
KEY_Sinh_tha: int = 16780717
KEY_Sinh_thha: int = 16780718
KEY_Sinh_tta: int = 16780711
KEY_Sinh_ttha: int = 16780712
KEY_Sinh_u: int = 16780683
KEY_Sinh_u2: int = 16780756
KEY_Sinh_uu: int = 16780684
KEY_Sinh_uu2: int = 16780758
KEY_Sinh_va: int = 16780736
KEY_Sinh_ya: int = 16780730
KEY_Sleep: int = 269025071
KEY_SlowKeys_Enable: int = 65139
KEY_Spell: int = 269025148
KEY_SplitScreen: int = 269025149
KEY_Standby: int = 269025040
KEY_Start: int = 269025050
KEY_StickyKeys_Enable: int = 65141
KEY_Stop: int = 269025064
KEY_Subtitle: int = 269025178
KEY_Super_L: int = 65515
KEY_Super_R: int = 65516
KEY_Support: int = 269025150
KEY_Suspend: int = 269025191
KEY_Switch_VT_1: int = 269024769
KEY_Switch_VT_10: int = 269024778
KEY_Switch_VT_11: int = 269024779
KEY_Switch_VT_12: int = 269024780
KEY_Switch_VT_2: int = 269024770
KEY_Switch_VT_3: int = 269024771
KEY_Switch_VT_4: int = 269024772
KEY_Switch_VT_5: int = 269024773
KEY_Switch_VT_6: int = 269024774
KEY_Switch_VT_7: int = 269024775
KEY_Switch_VT_8: int = 269024776
KEY_Switch_VT_9: int = 269024777
KEY_Sys_Req: int = 65301
KEY_T: int = 84
KEY_THORN: int = 222
KEY_Tab: int = 65289
KEY_Tabovedot: int = 16785002
KEY_TaskPane: int = 269025151
KEY_Tcaron: int = 427
KEY_Tcedilla: int = 478
KEY_Terminal: int = 269025152
KEY_Terminate_Server: int = 65237
KEY_Thai_baht: int = 3551
KEY_Thai_bobaimai: int = 3514
KEY_Thai_chochan: int = 3496
KEY_Thai_chochang: int = 3498
KEY_Thai_choching: int = 3497
KEY_Thai_chochoe: int = 3500
KEY_Thai_dochada: int = 3502
KEY_Thai_dodek: int = 3508
KEY_Thai_fofa: int = 3517
KEY_Thai_fofan: int = 3519
KEY_Thai_hohip: int = 3531
KEY_Thai_honokhuk: int = 3534
KEY_Thai_khokhai: int = 3490
KEY_Thai_khokhon: int = 3493
KEY_Thai_khokhuat: int = 3491
KEY_Thai_khokhwai: int = 3492
KEY_Thai_khorakhang: int = 3494
KEY_Thai_kokai: int = 3489
KEY_Thai_lakkhangyao: int = 3557
KEY_Thai_lekchet: int = 3575
KEY_Thai_lekha: int = 3573
KEY_Thai_lekhok: int = 3574
KEY_Thai_lekkao: int = 3577
KEY_Thai_leknung: int = 3569
KEY_Thai_lekpaet: int = 3576
KEY_Thai_leksam: int = 3571
KEY_Thai_leksi: int = 3572
KEY_Thai_leksong: int = 3570
KEY_Thai_leksun: int = 3568
KEY_Thai_lochula: int = 3532
KEY_Thai_loling: int = 3525
KEY_Thai_lu: int = 3526
KEY_Thai_maichattawa: int = 3563
KEY_Thai_maiek: int = 3560
KEY_Thai_maihanakat: int = 3537
KEY_Thai_maihanakat_maitho: int = 3550
KEY_Thai_maitaikhu: int = 3559
KEY_Thai_maitho: int = 3561
KEY_Thai_maitri: int = 3562
KEY_Thai_maiyamok: int = 3558
KEY_Thai_moma: int = 3521
KEY_Thai_ngongu: int = 3495
KEY_Thai_nikhahit: int = 3565
KEY_Thai_nonen: int = 3507
KEY_Thai_nonu: int = 3513
KEY_Thai_oang: int = 3533
KEY_Thai_paiyannoi: int = 3535
KEY_Thai_phinthu: int = 3546
KEY_Thai_phophan: int = 3518
KEY_Thai_phophung: int = 3516
KEY_Thai_phosamphao: int = 3520
KEY_Thai_popla: int = 3515
KEY_Thai_rorua: int = 3523
KEY_Thai_ru: int = 3524
KEY_Thai_saraa: int = 3536
KEY_Thai_saraaa: int = 3538
KEY_Thai_saraae: int = 3553
KEY_Thai_saraaimaimalai: int = 3556
KEY_Thai_saraaimaimuan: int = 3555
KEY_Thai_saraam: int = 3539
KEY_Thai_sarae: int = 3552
KEY_Thai_sarai: int = 3540
KEY_Thai_saraii: int = 3541
KEY_Thai_sarao: int = 3554
KEY_Thai_sarau: int = 3544
KEY_Thai_saraue: int = 3542
KEY_Thai_sarauee: int = 3543
KEY_Thai_sarauu: int = 3545
KEY_Thai_sorusi: int = 3529
KEY_Thai_sosala: int = 3528
KEY_Thai_soso: int = 3499
KEY_Thai_sosua: int = 3530
KEY_Thai_thanthakhat: int = 3564
KEY_Thai_thonangmontho: int = 3505
KEY_Thai_thophuthao: int = 3506
KEY_Thai_thothahan: int = 3511
KEY_Thai_thothan: int = 3504
KEY_Thai_thothong: int = 3512
KEY_Thai_thothung: int = 3510
KEY_Thai_topatak: int = 3503
KEY_Thai_totao: int = 3509
KEY_Thai_wowaen: int = 3527
KEY_Thai_yoyak: int = 3522
KEY_Thai_yoying: int = 3501
KEY_Thorn: int = 222
KEY_Time: int = 269025183
KEY_ToDoList: int = 269025055
KEY_Tools: int = 269025153
KEY_TopMenu: int = 269025186
KEY_TouchpadOff: int = 269025201
KEY_TouchpadOn: int = 269025200
KEY_TouchpadToggle: int = 269025193
KEY_Touroku: int = 65323
KEY_Travel: int = 269025154
KEY_Tslash: int = 940
KEY_U: int = 85
KEY_UWB: int = 269025174
KEY_Uacute: int = 218
KEY_Ubelowdot: int = 16785124
KEY_Ubreve: int = 733
KEY_Ucircumflex: int = 219
KEY_Udiaeresis: int = 220
KEY_Udoubleacute: int = 475
KEY_Ugrave: int = 217
KEY_Uhook: int = 16785126
KEY_Uhorn: int = 16777647
KEY_Uhornacute: int = 16785128
KEY_Uhornbelowdot: int = 16785136
KEY_Uhorngrave: int = 16785130
KEY_Uhornhook: int = 16785132
KEY_Uhorntilde: int = 16785134
KEY_Ukrainian_GHE_WITH_UPTURN: int = 1725
KEY_Ukrainian_I: int = 1718
KEY_Ukrainian_IE: int = 1716
KEY_Ukrainian_YI: int = 1719
KEY_Ukrainian_ghe_with_upturn: int = 1709
KEY_Ukrainian_i: int = 1702
KEY_Ukrainian_ie: int = 1700
KEY_Ukrainian_yi: int = 1703
KEY_Ukranian_I: int = 1718
KEY_Ukranian_JE: int = 1716
KEY_Ukranian_YI: int = 1719
KEY_Ukranian_i: int = 1702
KEY_Ukranian_je: int = 1700
KEY_Ukranian_yi: int = 1703
KEY_Umacron: int = 990
KEY_Undo: int = 65381
KEY_Ungrab: int = 269024800
KEY_Uogonek: int = 985
KEY_Up: int = 65362
KEY_Uring: int = 473
KEY_User1KB: int = 269025157
KEY_User2KB: int = 269025158
KEY_UserPB: int = 269025156
KEY_Utilde: int = 989
KEY_V: int = 86
KEY_VendorHome: int = 269025076
KEY_Video: int = 269025159
KEY_View: int = 269025185
KEY_VoidSymbol: int = 16777215
KEY_W: int = 87
KEY_WLAN: int = 269025173
KEY_WWAN: int = 269025204
KEY_WWW: int = 269025070
KEY_Wacute: int = 16785026
KEY_WakeUp: int = 269025067
KEY_Wcircumflex: int = 16777588
KEY_Wdiaeresis: int = 16785028
KEY_WebCam: int = 269025167
KEY_Wgrave: int = 16785024
KEY_WheelButton: int = 269025160
KEY_WindowClear: int = 269025109
KEY_WonSign: int = 16785577
KEY_Word: int = 269025161
KEY_X: int = 88
KEY_Xabovedot: int = 16785034
KEY_Xfer: int = 269025162
KEY_Y: int = 89
KEY_Yacute: int = 221
KEY_Ybelowdot: int = 16785140
KEY_Ycircumflex: int = 16777590
KEY_Ydiaeresis: int = 5054
KEY_Yellow: int = 269025189
KEY_Ygrave: int = 16785138
KEY_Yhook: int = 16785142
KEY_Ytilde: int = 16785144
KEY_Z: int = 90
KEY_Zabovedot: int = 431
KEY_Zacute: int = 428
KEY_Zcaron: int = 430
KEY_Zen_Koho: int = 65341
KEY_Zenkaku: int = 65320
KEY_Zenkaku_Hankaku: int = 65322
KEY_ZoomIn: int = 269025163
KEY_ZoomOut: int = 269025164
KEY_Zstroke: int = 16777653
KEY_a: int = 97
KEY_aacute: int = 225
KEY_abelowdot: int = 16785057
KEY_abovedot: int = 511
KEY_abreve: int = 483
KEY_abreveacute: int = 16785071
KEY_abrevebelowdot: int = 16785079
KEY_abrevegrave: int = 16785073
KEY_abrevehook: int = 16785075
KEY_abrevetilde: int = 16785077
KEY_acircumflex: int = 226
KEY_acircumflexacute: int = 16785061
KEY_acircumflexbelowdot: int = 16785069
KEY_acircumflexgrave: int = 16785063
KEY_acircumflexhook: int = 16785065
KEY_acircumflextilde: int = 16785067
KEY_acute: int = 180
KEY_adiaeresis: int = 228
KEY_ae: int = 230
KEY_agrave: int = 224
KEY_ahook: int = 16785059
KEY_amacron: int = 992
KEY_ampersand: int = 38
KEY_aogonek: int = 433
KEY_apostrophe: int = 39
KEY_approxeq: int = 16785992
KEY_approximate: int = 2248
KEY_aring: int = 229
KEY_asciicircum: int = 94
KEY_asciitilde: int = 126
KEY_asterisk: int = 42
KEY_at: int = 64
KEY_atilde: int = 227
KEY_b: int = 98
KEY_babovedot: int = 16784899
KEY_backslash: int = 92
KEY_ballotcross: int = 2804
KEY_bar: int = 124
KEY_because: int = 16785973
KEY_blank: int = 2527
KEY_botintegral: int = 2213
KEY_botleftparens: int = 2220
KEY_botleftsqbracket: int = 2216
KEY_botleftsummation: int = 2226
KEY_botrightparens: int = 2222
KEY_botrightsqbracket: int = 2218
KEY_botrightsummation: int = 2230
KEY_bott: int = 2550
KEY_botvertsummationconnector: int = 2228
KEY_braceleft: int = 123
KEY_braceright: int = 125
KEY_bracketleft: int = 91
KEY_bracketright: int = 93
KEY_braille_blank: int = 16787456
KEY_braille_dot_1: int = 65521
KEY_braille_dot_10: int = 65530
KEY_braille_dot_2: int = 65522
KEY_braille_dot_3: int = 65523
KEY_braille_dot_4: int = 65524
KEY_braille_dot_5: int = 65525
KEY_braille_dot_6: int = 65526
KEY_braille_dot_7: int = 65527
KEY_braille_dot_8: int = 65528
KEY_braille_dot_9: int = 65529
KEY_braille_dots_1: int = 16787457
KEY_braille_dots_12: int = 16787459
KEY_braille_dots_123: int = 16787463
KEY_braille_dots_1234: int = 16787471
KEY_braille_dots_12345: int = 16787487
KEY_braille_dots_123456: int = 16787519
KEY_braille_dots_1234567: int = 16787583
KEY_braille_dots_12345678: int = 16787711
KEY_braille_dots_1234568: int = 16787647
KEY_braille_dots_123457: int = 16787551
KEY_braille_dots_1234578: int = 16787679
KEY_braille_dots_123458: int = 16787615
KEY_braille_dots_12346: int = 16787503
KEY_braille_dots_123467: int = 16787567
KEY_braille_dots_1234678: int = 16787695
KEY_braille_dots_123468: int = 16787631
KEY_braille_dots_12347: int = 16787535
KEY_braille_dots_123478: int = 16787663
KEY_braille_dots_12348: int = 16787599
KEY_braille_dots_1235: int = 16787479
KEY_braille_dots_12356: int = 16787511
KEY_braille_dots_123567: int = 16787575
KEY_braille_dots_1235678: int = 16787703
KEY_braille_dots_123568: int = 16787639
KEY_braille_dots_12357: int = 16787543
KEY_braille_dots_123578: int = 16787671
KEY_braille_dots_12358: int = 16787607
KEY_braille_dots_1236: int = 16787495
KEY_braille_dots_12367: int = 16787559
KEY_braille_dots_123678: int = 16787687
KEY_braille_dots_12368: int = 16787623
KEY_braille_dots_1237: int = 16787527
KEY_braille_dots_12378: int = 16787655
KEY_braille_dots_1238: int = 16787591
KEY_braille_dots_124: int = 16787467
KEY_braille_dots_1245: int = 16787483
KEY_braille_dots_12456: int = 16787515
KEY_braille_dots_124567: int = 16787579
KEY_braille_dots_1245678: int = 16787707
KEY_braille_dots_124568: int = 16787643
KEY_braille_dots_12457: int = 16787547
KEY_braille_dots_124578: int = 16787675
KEY_braille_dots_12458: int = 16787611
KEY_braille_dots_1246: int = 16787499
KEY_braille_dots_12467: int = 16787563
KEY_braille_dots_124678: int = 16787691
KEY_braille_dots_12468: int = 16787627
KEY_braille_dots_1247: int = 16787531
KEY_braille_dots_12478: int = 16787659
KEY_braille_dots_1248: int = 16787595
KEY_braille_dots_125: int = 16787475
KEY_braille_dots_1256: int = 16787507
KEY_braille_dots_12567: int = 16787571
KEY_braille_dots_125678: int = 16787699
KEY_braille_dots_12568: int = 16787635
KEY_braille_dots_1257: int = 16787539
KEY_braille_dots_12578: int = 16787667
KEY_braille_dots_1258: int = 16787603
KEY_braille_dots_126: int = 16787491
KEY_braille_dots_1267: int = 16787555
KEY_braille_dots_12678: int = 16787683
KEY_braille_dots_1268: int = 16787619
KEY_braille_dots_127: int = 16787523
KEY_braille_dots_1278: int = 16787651
KEY_braille_dots_128: int = 16787587
KEY_braille_dots_13: int = 16787461
KEY_braille_dots_134: int = 16787469
KEY_braille_dots_1345: int = 16787485
KEY_braille_dots_13456: int = 16787517
KEY_braille_dots_134567: int = 16787581
KEY_braille_dots_1345678: int = 16787709
KEY_braille_dots_134568: int = 16787645
KEY_braille_dots_13457: int = 16787549
KEY_braille_dots_134578: int = 16787677
KEY_braille_dots_13458: int = 16787613
KEY_braille_dots_1346: int = 16787501
KEY_braille_dots_13467: int = 16787565
KEY_braille_dots_134678: int = 16787693
KEY_braille_dots_13468: int = 16787629
KEY_braille_dots_1347: int = 16787533
KEY_braille_dots_13478: int = 16787661
KEY_braille_dots_1348: int = 16787597
KEY_braille_dots_135: int = 16787477
KEY_braille_dots_1356: int = 16787509
KEY_braille_dots_13567: int = 16787573
KEY_braille_dots_135678: int = 16787701
KEY_braille_dots_13568: int = 16787637
KEY_braille_dots_1357: int = 16787541
KEY_braille_dots_13578: int = 16787669
KEY_braille_dots_1358: int = 16787605
KEY_braille_dots_136: int = 16787493
KEY_braille_dots_1367: int = 16787557
KEY_braille_dots_13678: int = 16787685
KEY_braille_dots_1368: int = 16787621
KEY_braille_dots_137: int = 16787525
KEY_braille_dots_1378: int = 16787653
KEY_braille_dots_138: int = 16787589
KEY_braille_dots_14: int = 16787465
KEY_braille_dots_145: int = 16787481
KEY_braille_dots_1456: int = 16787513
KEY_braille_dots_14567: int = 16787577
KEY_braille_dots_145678: int = 16787705
KEY_braille_dots_14568: int = 16787641
KEY_braille_dots_1457: int = 16787545
KEY_braille_dots_14578: int = 16787673
KEY_braille_dots_1458: int = 16787609
KEY_braille_dots_146: int = 16787497
KEY_braille_dots_1467: int = 16787561
KEY_braille_dots_14678: int = 16787689
KEY_braille_dots_1468: int = 16787625
KEY_braille_dots_147: int = 16787529
KEY_braille_dots_1478: int = 16787657
KEY_braille_dots_148: int = 16787593
KEY_braille_dots_15: int = 16787473
KEY_braille_dots_156: int = 16787505
KEY_braille_dots_1567: int = 16787569
KEY_braille_dots_15678: int = 16787697
KEY_braille_dots_1568: int = 16787633
KEY_braille_dots_157: int = 16787537
KEY_braille_dots_1578: int = 16787665
KEY_braille_dots_158: int = 16787601
KEY_braille_dots_16: int = 16787489
KEY_braille_dots_167: int = 16787553
KEY_braille_dots_1678: int = 16787681
KEY_braille_dots_168: int = 16787617
KEY_braille_dots_17: int = 16787521
KEY_braille_dots_178: int = 16787649
KEY_braille_dots_18: int = 16787585
KEY_braille_dots_2: int = 16787458
KEY_braille_dots_23: int = 16787462
KEY_braille_dots_234: int = 16787470
KEY_braille_dots_2345: int = 16787486
KEY_braille_dots_23456: int = 16787518
KEY_braille_dots_234567: int = 16787582
KEY_braille_dots_2345678: int = 16787710
KEY_braille_dots_234568: int = 16787646
KEY_braille_dots_23457: int = 16787550
KEY_braille_dots_234578: int = 16787678
KEY_braille_dots_23458: int = 16787614
KEY_braille_dots_2346: int = 16787502
KEY_braille_dots_23467: int = 16787566
KEY_braille_dots_234678: int = 16787694
KEY_braille_dots_23468: int = 16787630
KEY_braille_dots_2347: int = 16787534
KEY_braille_dots_23478: int = 16787662
KEY_braille_dots_2348: int = 16787598
KEY_braille_dots_235: int = 16787478
KEY_braille_dots_2356: int = 16787510
KEY_braille_dots_23567: int = 16787574
KEY_braille_dots_235678: int = 16787702
KEY_braille_dots_23568: int = 16787638
KEY_braille_dots_2357: int = 16787542
KEY_braille_dots_23578: int = 16787670
KEY_braille_dots_2358: int = 16787606
KEY_braille_dots_236: int = 16787494
KEY_braille_dots_2367: int = 16787558
KEY_braille_dots_23678: int = 16787686
KEY_braille_dots_2368: int = 16787622
KEY_braille_dots_237: int = 16787526
KEY_braille_dots_2378: int = 16787654
KEY_braille_dots_238: int = 16787590
KEY_braille_dots_24: int = 16787466
KEY_braille_dots_245: int = 16787482
KEY_braille_dots_2456: int = 16787514
KEY_braille_dots_24567: int = 16787578
KEY_braille_dots_245678: int = 16787706
KEY_braille_dots_24568: int = 16787642
KEY_braille_dots_2457: int = 16787546
KEY_braille_dots_24578: int = 16787674
KEY_braille_dots_2458: int = 16787610
KEY_braille_dots_246: int = 16787498
KEY_braille_dots_2467: int = 16787562
KEY_braille_dots_24678: int = 16787690
KEY_braille_dots_2468: int = 16787626
KEY_braille_dots_247: int = 16787530
KEY_braille_dots_2478: int = 16787658
KEY_braille_dots_248: int = 16787594
KEY_braille_dots_25: int = 16787474
KEY_braille_dots_256: int = 16787506
KEY_braille_dots_2567: int = 16787570
KEY_braille_dots_25678: int = 16787698
KEY_braille_dots_2568: int = 16787634
KEY_braille_dots_257: int = 16787538
KEY_braille_dots_2578: int = 16787666
KEY_braille_dots_258: int = 16787602
KEY_braille_dots_26: int = 16787490
KEY_braille_dots_267: int = 16787554
KEY_braille_dots_2678: int = 16787682
KEY_braille_dots_268: int = 16787618
KEY_braille_dots_27: int = 16787522
KEY_braille_dots_278: int = 16787650
KEY_braille_dots_28: int = 16787586
KEY_braille_dots_3: int = 16787460
KEY_braille_dots_34: int = 16787468
KEY_braille_dots_345: int = 16787484
KEY_braille_dots_3456: int = 16787516
KEY_braille_dots_34567: int = 16787580
KEY_braille_dots_345678: int = 16787708
KEY_braille_dots_34568: int = 16787644
KEY_braille_dots_3457: int = 16787548
KEY_braille_dots_34578: int = 16787676
KEY_braille_dots_3458: int = 16787612
KEY_braille_dots_346: int = 16787500
KEY_braille_dots_3467: int = 16787564
KEY_braille_dots_34678: int = 16787692
KEY_braille_dots_3468: int = 16787628
KEY_braille_dots_347: int = 16787532
KEY_braille_dots_3478: int = 16787660
KEY_braille_dots_348: int = 16787596
KEY_braille_dots_35: int = 16787476
KEY_braille_dots_356: int = 16787508
KEY_braille_dots_3567: int = 16787572
KEY_braille_dots_35678: int = 16787700
KEY_braille_dots_3568: int = 16787636
KEY_braille_dots_357: int = 16787540
KEY_braille_dots_3578: int = 16787668
KEY_braille_dots_358: int = 16787604
KEY_braille_dots_36: int = 16787492
KEY_braille_dots_367: int = 16787556
KEY_braille_dots_3678: int = 16787684
KEY_braille_dots_368: int = 16787620
KEY_braille_dots_37: int = 16787524
KEY_braille_dots_378: int = 16787652
KEY_braille_dots_38: int = 16787588
KEY_braille_dots_4: int = 16787464
KEY_braille_dots_45: int = 16787480
KEY_braille_dots_456: int = 16787512
KEY_braille_dots_4567: int = 16787576
KEY_braille_dots_45678: int = 16787704
KEY_braille_dots_4568: int = 16787640
KEY_braille_dots_457: int = 16787544
KEY_braille_dots_4578: int = 16787672
KEY_braille_dots_458: int = 16787608
KEY_braille_dots_46: int = 16787496
KEY_braille_dots_467: int = 16787560
KEY_braille_dots_4678: int = 16787688
KEY_braille_dots_468: int = 16787624
KEY_braille_dots_47: int = 16787528
KEY_braille_dots_478: int = 16787656
KEY_braille_dots_48: int = 16787592
KEY_braille_dots_5: int = 16787472
KEY_braille_dots_56: int = 16787504
KEY_braille_dots_567: int = 16787568
KEY_braille_dots_5678: int = 16787696
KEY_braille_dots_568: int = 16787632
KEY_braille_dots_57: int = 16787536
KEY_braille_dots_578: int = 16787664
KEY_braille_dots_58: int = 16787600
KEY_braille_dots_6: int = 16787488
KEY_braille_dots_67: int = 16787552
KEY_braille_dots_678: int = 16787680
KEY_braille_dots_68: int = 16787616
KEY_braille_dots_7: int = 16787520
KEY_braille_dots_78: int = 16787648
KEY_braille_dots_8: int = 16787584
KEY_breve: int = 418
KEY_brokenbar: int = 166
KEY_c: int = 99
KEY_c_h: int = 65187
KEY_cabovedot: int = 741
KEY_cacute: int = 486
KEY_careof: int = 2744
KEY_caret: int = 2812
KEY_caron: int = 439
KEY_ccaron: int = 488
KEY_ccedilla: int = 231
KEY_ccircumflex: int = 742
KEY_cedilla: int = 184
KEY_cent: int = 162
KEY_ch: int = 65184
KEY_checkerboard: int = 2529
KEY_checkmark: int = 2803
KEY_circle: int = 3023
KEY_club: int = 2796
KEY_colon: int = 58
KEY_comma: int = 44
KEY_containsas: int = 16785931
KEY_copyright: int = 169
KEY_cr: int = 2532
KEY_crossinglines: int = 2542
KEY_cuberoot: int = 16785947
KEY_currency: int = 164
KEY_cursor: int = 2815
KEY_d: int = 100
KEY_dabovedot: int = 16784907
KEY_dagger: int = 2801
KEY_dcaron: int = 495
KEY_dead_A: int = 65153
KEY_dead_E: int = 65155
KEY_dead_I: int = 65157
KEY_dead_O: int = 65159
KEY_dead_U: int = 65161
KEY_dead_a: int = 65152
KEY_dead_abovecomma: int = 65124
KEY_dead_abovedot: int = 65110
KEY_dead_abovereversedcomma: int = 65125
KEY_dead_abovering: int = 65112
KEY_dead_aboveverticalline: int = 65169
KEY_dead_acute: int = 65105
KEY_dead_belowbreve: int = 65131
KEY_dead_belowcircumflex: int = 65129
KEY_dead_belowcomma: int = 65134
KEY_dead_belowdiaeresis: int = 65132
KEY_dead_belowdot: int = 65120
KEY_dead_belowmacron: int = 65128
KEY_dead_belowring: int = 65127
KEY_dead_belowtilde: int = 65130
KEY_dead_belowverticalline: int = 65170
KEY_dead_breve: int = 65109
KEY_dead_capital_schwa: int = 65163
KEY_dead_caron: int = 65114
KEY_dead_cedilla: int = 65115
KEY_dead_circumflex: int = 65106
KEY_dead_currency: int = 65135
KEY_dead_dasia: int = 65125
KEY_dead_diaeresis: int = 65111
KEY_dead_doubleacute: int = 65113
KEY_dead_doublegrave: int = 65126
KEY_dead_e: int = 65154
KEY_dead_grave: int = 65104
KEY_dead_greek: int = 65164
KEY_dead_hook: int = 65121
KEY_dead_horn: int = 65122
KEY_dead_i: int = 65156
KEY_dead_invertedbreve: int = 65133
KEY_dead_iota: int = 65117
KEY_dead_longsolidusoverlay: int = 65171
KEY_dead_lowline: int = 65168
KEY_dead_macron: int = 65108
KEY_dead_o: int = 65158
KEY_dead_ogonek: int = 65116
KEY_dead_perispomeni: int = 65107
KEY_dead_psili: int = 65124
KEY_dead_semivoiced_sound: int = 65119
KEY_dead_small_schwa: int = 65162
KEY_dead_stroke: int = 65123
KEY_dead_tilde: int = 65107
KEY_dead_u: int = 65160
KEY_dead_voiced_sound: int = 65118
KEY_decimalpoint: int = 2749
KEY_degree: int = 176
KEY_diaeresis: int = 168
KEY_diamond: int = 2797
KEY_digitspace: int = 2725
KEY_dintegral: int = 16785964
KEY_division: int = 247
KEY_dollar: int = 36
KEY_doubbaselinedot: int = 2735
KEY_doubleacute: int = 445
KEY_doubledagger: int = 2802
KEY_doublelowquotemark: int = 2814
KEY_downarrow: int = 2302
KEY_downcaret: int = 2984
KEY_downshoe: int = 3030
KEY_downstile: int = 3012
KEY_downtack: int = 3010
KEY_dstroke: int = 496
KEY_e: int = 101
KEY_eabovedot: int = 1004
KEY_eacute: int = 233
KEY_ebelowdot: int = 16785081
KEY_ecaron: int = 492
KEY_ecircumflex: int = 234
KEY_ecircumflexacute: int = 16785087
KEY_ecircumflexbelowdot: int = 16785095
KEY_ecircumflexgrave: int = 16785089
KEY_ecircumflexhook: int = 16785091
KEY_ecircumflextilde: int = 16785093
KEY_ediaeresis: int = 235
KEY_egrave: int = 232
KEY_ehook: int = 16785083
KEY_eightsubscript: int = 16785544
KEY_eightsuperior: int = 16785528
KEY_elementof: int = 16785928
KEY_ellipsis: int = 2734
KEY_em3space: int = 2723
KEY_em4space: int = 2724
KEY_emacron: int = 954
KEY_emdash: int = 2729
KEY_emfilledcircle: int = 2782
KEY_emfilledrect: int = 2783
KEY_emopencircle: int = 2766
KEY_emopenrectangle: int = 2767
KEY_emptyset: int = 16785925
KEY_emspace: int = 2721
KEY_endash: int = 2730
KEY_enfilledcircbullet: int = 2790
KEY_enfilledsqbullet: int = 2791
KEY_eng: int = 959
KEY_enopencircbullet: int = 2784
KEY_enopensquarebullet: int = 2785
KEY_enspace: int = 2722
KEY_eogonek: int = 490
KEY_equal: int = 61
KEY_eth: int = 240
KEY_etilde: int = 16785085
KEY_exclam: int = 33
KEY_exclamdown: int = 161
KEY_ezh: int = 16777874
KEY_f: int = 102
KEY_fabovedot: int = 16784927
KEY_femalesymbol: int = 2808
KEY_ff: int = 2531
KEY_figdash: int = 2747
KEY_filledlefttribullet: int = 2780
KEY_filledrectbullet: int = 2779
KEY_filledrighttribullet: int = 2781
KEY_filledtribulletdown: int = 2793
KEY_filledtribulletup: int = 2792
KEY_fiveeighths: int = 2757
KEY_fivesixths: int = 2743
KEY_fivesubscript: int = 16785541
KEY_fivesuperior: int = 16785525
KEY_fourfifths: int = 2741
KEY_foursubscript: int = 16785540
KEY_foursuperior: int = 16785524
KEY_fourthroot: int = 16785948
KEY_function: int = 2294
KEY_g: int = 103
KEY_gabovedot: int = 757
KEY_gbreve: int = 699
KEY_gcaron: int = 16777703
KEY_gcedilla: int = 955
KEY_gcircumflex: int = 760
KEY_grave: int = 96
KEY_greater: int = 62
KEY_greaterthanequal: int = 2238
KEY_guillemotleft: int = 171
KEY_guillemotright: int = 187
KEY_h: int = 104
KEY_hairspace: int = 2728
KEY_hcircumflex: int = 694
KEY_heart: int = 2798
KEY_hebrew_aleph: int = 3296
KEY_hebrew_ayin: int = 3314
KEY_hebrew_bet: int = 3297
KEY_hebrew_beth: int = 3297
KEY_hebrew_chet: int = 3303
KEY_hebrew_dalet: int = 3299
KEY_hebrew_daleth: int = 3299
KEY_hebrew_doublelowline: int = 3295
KEY_hebrew_finalkaph: int = 3306
KEY_hebrew_finalmem: int = 3309
KEY_hebrew_finalnun: int = 3311
KEY_hebrew_finalpe: int = 3315
KEY_hebrew_finalzade: int = 3317
KEY_hebrew_finalzadi: int = 3317
KEY_hebrew_gimel: int = 3298
KEY_hebrew_gimmel: int = 3298
KEY_hebrew_he: int = 3300
KEY_hebrew_het: int = 3303
KEY_hebrew_kaph: int = 3307
KEY_hebrew_kuf: int = 3319
KEY_hebrew_lamed: int = 3308
KEY_hebrew_mem: int = 3310
KEY_hebrew_nun: int = 3312
KEY_hebrew_pe: int = 3316
KEY_hebrew_qoph: int = 3319
KEY_hebrew_resh: int = 3320
KEY_hebrew_samech: int = 3313
KEY_hebrew_samekh: int = 3313
KEY_hebrew_shin: int = 3321
KEY_hebrew_taf: int = 3322
KEY_hebrew_taw: int = 3322
KEY_hebrew_tet: int = 3304
KEY_hebrew_teth: int = 3304
KEY_hebrew_waw: int = 3301
KEY_hebrew_yod: int = 3305
KEY_hebrew_zade: int = 3318
KEY_hebrew_zadi: int = 3318
KEY_hebrew_zain: int = 3302
KEY_hebrew_zayin: int = 3302
KEY_hexagram: int = 2778
KEY_horizconnector: int = 2211
KEY_horizlinescan1: int = 2543
KEY_horizlinescan3: int = 2544
KEY_horizlinescan5: int = 2545
KEY_horizlinescan7: int = 2546
KEY_horizlinescan9: int = 2547
KEY_hstroke: int = 689
KEY_ht: int = 2530
KEY_hyphen: int = 173
KEY_i: int = 105
KEY_iTouch: int = 269025120
KEY_iacute: int = 237
KEY_ibelowdot: int = 16785099
KEY_ibreve: int = 16777517
KEY_icircumflex: int = 238
KEY_identical: int = 2255
KEY_idiaeresis: int = 239
KEY_idotless: int = 697
KEY_ifonlyif: int = 2253
KEY_igrave: int = 236
KEY_ihook: int = 16785097
KEY_imacron: int = 1007
KEY_implies: int = 2254
KEY_includedin: int = 2266
KEY_includes: int = 2267
KEY_infinity: int = 2242
KEY_integral: int = 2239
KEY_intersection: int = 2268
KEY_iogonek: int = 999
KEY_itilde: int = 949
KEY_j: int = 106
KEY_jcircumflex: int = 700
KEY_jot: int = 3018
KEY_k: int = 107
KEY_kana_A: int = 1201
KEY_kana_CHI: int = 1217
KEY_kana_E: int = 1204
KEY_kana_FU: int = 1228
KEY_kana_HA: int = 1226
KEY_kana_HE: int = 1229
KEY_kana_HI: int = 1227
KEY_kana_HO: int = 1230
KEY_kana_HU: int = 1228
KEY_kana_I: int = 1202
KEY_kana_KA: int = 1206
KEY_kana_KE: int = 1209
KEY_kana_KI: int = 1207
KEY_kana_KO: int = 1210
KEY_kana_KU: int = 1208
KEY_kana_MA: int = 1231
KEY_kana_ME: int = 1234
KEY_kana_MI: int = 1232
KEY_kana_MO: int = 1235
KEY_kana_MU: int = 1233
KEY_kana_N: int = 1245
KEY_kana_NA: int = 1221
KEY_kana_NE: int = 1224
KEY_kana_NI: int = 1222
KEY_kana_NO: int = 1225
KEY_kana_NU: int = 1223
KEY_kana_O: int = 1205
KEY_kana_RA: int = 1239
KEY_kana_RE: int = 1242
KEY_kana_RI: int = 1240
KEY_kana_RO: int = 1243
KEY_kana_RU: int = 1241
KEY_kana_SA: int = 1211
KEY_kana_SE: int = 1214
KEY_kana_SHI: int = 1212
KEY_kana_SO: int = 1215
KEY_kana_SU: int = 1213
KEY_kana_TA: int = 1216
KEY_kana_TE: int = 1219
KEY_kana_TI: int = 1217
KEY_kana_TO: int = 1220
KEY_kana_TSU: int = 1218
KEY_kana_TU: int = 1218
KEY_kana_U: int = 1203
KEY_kana_WA: int = 1244
KEY_kana_WO: int = 1190
KEY_kana_YA: int = 1236
KEY_kana_YO: int = 1238
KEY_kana_YU: int = 1237
KEY_kana_a: int = 1191
KEY_kana_closingbracket: int = 1187
KEY_kana_comma: int = 1188
KEY_kana_conjunctive: int = 1189
KEY_kana_e: int = 1194
KEY_kana_fullstop: int = 1185
KEY_kana_i: int = 1192
KEY_kana_middledot: int = 1189
KEY_kana_o: int = 1195
KEY_kana_openingbracket: int = 1186
KEY_kana_switch: int = 65406
KEY_kana_tsu: int = 1199
KEY_kana_tu: int = 1199
KEY_kana_u: int = 1193
KEY_kana_ya: int = 1196
KEY_kana_yo: int = 1198
KEY_kana_yu: int = 1197
KEY_kappa: int = 930
KEY_kcedilla: int = 1011
KEY_kra: int = 930
KEY_l: int = 108
KEY_lacute: int = 485
KEY_latincross: int = 2777
KEY_lbelowdot: int = 16784951
KEY_lcaron: int = 437
KEY_lcedilla: int = 950
KEY_leftanglebracket: int = 2748
KEY_leftarrow: int = 2299
KEY_leftcaret: int = 2979
KEY_leftdoublequotemark: int = 2770
KEY_leftmiddlecurlybrace: int = 2223
KEY_leftopentriangle: int = 2764
KEY_leftpointer: int = 2794
KEY_leftradical: int = 2209
KEY_leftshoe: int = 3034
KEY_leftsinglequotemark: int = 2768
KEY_leftt: int = 2548
KEY_lefttack: int = 3036
KEY_less: int = 60
KEY_lessthanequal: int = 2236
KEY_lf: int = 2533
KEY_logicaland: int = 2270
KEY_logicalor: int = 2271
KEY_lowleftcorner: int = 2541
KEY_lowrightcorner: int = 2538
KEY_lstroke: int = 435
KEY_m: int = 109
KEY_mabovedot: int = 16784961
KEY_macron: int = 175
KEY_malesymbol: int = 2807
KEY_maltesecross: int = 2800
KEY_marker: int = 2751
KEY_masculine: int = 186
KEY_minus: int = 45
KEY_minutes: int = 2774
KEY_mu: int = 181
KEY_multiply: int = 215
KEY_musicalflat: int = 2806
KEY_musicalsharp: int = 2805
KEY_n: int = 110
KEY_nabla: int = 2245
KEY_nacute: int = 497
KEY_ncaron: int = 498
KEY_ncedilla: int = 1009
KEY_ninesubscript: int = 16785545
KEY_ninesuperior: int = 16785529
KEY_nl: int = 2536
KEY_nobreakspace: int = 160
KEY_notapproxeq: int = 16785991
KEY_notelementof: int = 16785929
KEY_notequal: int = 2237
KEY_notidentical: int = 16786018
KEY_notsign: int = 172
KEY_ntilde: int = 241
KEY_numbersign: int = 35
KEY_numerosign: int = 1712
KEY_o: int = 111
KEY_oacute: int = 243
KEY_obarred: int = 16777845
KEY_obelowdot: int = 16785101
KEY_ocaron: int = 16777682
KEY_ocircumflex: int = 244
KEY_ocircumflexacute: int = 16785105
KEY_ocircumflexbelowdot: int = 16785113
KEY_ocircumflexgrave: int = 16785107
KEY_ocircumflexhook: int = 16785109
KEY_ocircumflextilde: int = 16785111
KEY_odiaeresis: int = 246
KEY_odoubleacute: int = 501
KEY_oe: int = 5053
KEY_ogonek: int = 434
KEY_ograve: int = 242
KEY_ohook: int = 16785103
KEY_ohorn: int = 16777633
KEY_ohornacute: int = 16785115
KEY_ohornbelowdot: int = 16785123
KEY_ohorngrave: int = 16785117
KEY_ohornhook: int = 16785119
KEY_ohorntilde: int = 16785121
KEY_omacron: int = 1010
KEY_oneeighth: int = 2755
KEY_onefifth: int = 2738
KEY_onehalf: int = 189
KEY_onequarter: int = 188
KEY_onesixth: int = 2742
KEY_onesubscript: int = 16785537
KEY_onesuperior: int = 185
KEY_onethird: int = 2736
KEY_ooblique: int = 248
KEY_openrectbullet: int = 2786
KEY_openstar: int = 2789
KEY_opentribulletdown: int = 2788
KEY_opentribulletup: int = 2787
KEY_ordfeminine: int = 170
KEY_oslash: int = 248
KEY_otilde: int = 245
KEY_overbar: int = 3008
KEY_overline: int = 1150
KEY_p: int = 112
KEY_pabovedot: int = 16784983
KEY_paragraph: int = 182
KEY_parenleft: int = 40
KEY_parenright: int = 41
KEY_partdifferential: int = 16785922
KEY_partialderivative: int = 2287
KEY_percent: int = 37
KEY_period: int = 46
KEY_periodcentered: int = 183
KEY_permille: int = 2773
KEY_phonographcopyright: int = 2811
KEY_plus: int = 43
KEY_plusminus: int = 177
KEY_prescription: int = 2772
KEY_prolongedsound: int = 1200
KEY_punctspace: int = 2726
KEY_q: int = 113
KEY_quad: int = 3020
KEY_question: int = 63
KEY_questiondown: int = 191
KEY_quotedbl: int = 34
KEY_quoteleft: int = 96
KEY_quoteright: int = 39
KEY_r: int = 114
KEY_racute: int = 480
KEY_radical: int = 2262
KEY_rcaron: int = 504
KEY_rcedilla: int = 947
KEY_registered: int = 174
KEY_rightanglebracket: int = 2750
KEY_rightarrow: int = 2301
KEY_rightcaret: int = 2982
KEY_rightdoublequotemark: int = 2771
KEY_rightmiddlecurlybrace: int = 2224
KEY_rightmiddlesummation: int = 2231
KEY_rightopentriangle: int = 2765
KEY_rightpointer: int = 2795
KEY_rightshoe: int = 3032
KEY_rightsinglequotemark: int = 2769
KEY_rightt: int = 2549
KEY_righttack: int = 3068
KEY_s: int = 115
KEY_sabovedot: int = 16784993
KEY_sacute: int = 438
KEY_scaron: int = 441
KEY_scedilla: int = 442
KEY_schwa: int = 16777817
KEY_scircumflex: int = 766
KEY_script_switch: int = 65406
KEY_seconds: int = 2775
KEY_section: int = 167
KEY_semicolon: int = 59
KEY_semivoicedsound: int = 1247
KEY_seveneighths: int = 2758
KEY_sevensubscript: int = 16785543
KEY_sevensuperior: int = 16785527
KEY_signaturemark: int = 2762
KEY_signifblank: int = 2732
KEY_similarequal: int = 2249
KEY_singlelowquotemark: int = 2813
KEY_sixsubscript: int = 16785542
KEY_sixsuperior: int = 16785526
KEY_slash: int = 47
KEY_soliddiamond: int = 2528
KEY_space: int = 32
KEY_squareroot: int = 16785946
KEY_ssharp: int = 223
KEY_sterling: int = 163
KEY_stricteq: int = 16786019
KEY_t: int = 116
KEY_tabovedot: int = 16785003
KEY_tcaron: int = 443
KEY_tcedilla: int = 510
KEY_telephone: int = 2809
KEY_telephonerecorder: int = 2810
KEY_therefore: int = 2240
KEY_thinspace: int = 2727
KEY_thorn: int = 254
KEY_threeeighths: int = 2756
KEY_threefifths: int = 2740
KEY_threequarters: int = 190
KEY_threesubscript: int = 16785539
KEY_threesuperior: int = 179
KEY_tintegral: int = 16785965
KEY_topintegral: int = 2212
KEY_topleftparens: int = 2219
KEY_topleftradical: int = 2210
KEY_topleftsqbracket: int = 2215
KEY_topleftsummation: int = 2225
KEY_toprightparens: int = 2221
KEY_toprightsqbracket: int = 2217
KEY_toprightsummation: int = 2229
KEY_topt: int = 2551
KEY_topvertsummationconnector: int = 2227
KEY_trademark: int = 2761
KEY_trademarkincircle: int = 2763
KEY_tslash: int = 956
KEY_twofifths: int = 2739
KEY_twosubscript: int = 16785538
KEY_twosuperior: int = 178
KEY_twothirds: int = 2737
KEY_u: int = 117
KEY_uacute: int = 250
KEY_ubelowdot: int = 16785125
KEY_ubreve: int = 765
KEY_ucircumflex: int = 251
KEY_udiaeresis: int = 252
KEY_udoubleacute: int = 507
KEY_ugrave: int = 249
KEY_uhook: int = 16785127
KEY_uhorn: int = 16777648
KEY_uhornacute: int = 16785129
KEY_uhornbelowdot: int = 16785137
KEY_uhorngrave: int = 16785131
KEY_uhornhook: int = 16785133
KEY_uhorntilde: int = 16785135
KEY_umacron: int = 1022
KEY_underbar: int = 3014
KEY_underscore: int = 95
KEY_union: int = 2269
KEY_uogonek: int = 1017
KEY_uparrow: int = 2300
KEY_upcaret: int = 2985
KEY_upleftcorner: int = 2540
KEY_uprightcorner: int = 2539
KEY_upshoe: int = 3011
KEY_upstile: int = 3027
KEY_uptack: int = 3022
KEY_uring: int = 505
KEY_utilde: int = 1021
KEY_v: int = 118
KEY_variation: int = 2241
KEY_vertbar: int = 2552
KEY_vertconnector: int = 2214
KEY_voicedsound: int = 1246
KEY_vt: int = 2537
KEY_w: int = 119
KEY_wacute: int = 16785027
KEY_wcircumflex: int = 16777589
KEY_wdiaeresis: int = 16785029
KEY_wgrave: int = 16785025
KEY_x: int = 120
KEY_xabovedot: int = 16785035
KEY_y: int = 121
KEY_yacute: int = 253
KEY_ybelowdot: int = 16785141
KEY_ycircumflex: int = 16777591
KEY_ydiaeresis: int = 255
KEY_yen: int = 165
KEY_ygrave: int = 16785139
KEY_yhook: int = 16785143
KEY_ytilde: int = 16785145
KEY_z: int = 122
KEY_zabovedot: int = 447
KEY_zacute: int = 444
KEY_zcaron: int = 446
KEY_zerosubscript: int = 16785536
KEY_zerosuperior: int = 16785520
KEY_zstroke: int = 16777654
KP_0: int = 65456
KP_1: int = 65457
KP_2: int = 65458
KP_3: int = 65459
KP_4: int = 65460
KP_5: int = 65461
KP_6: int = 65462
KP_7: int = 65463
KP_8: int = 65464
KP_9: int = 65465
KP_Add: int = 65451
KP_Begin: int = 65437
KP_Decimal: int = 65454
KP_Delete: int = 65439
KP_Divide: int = 65455
KP_Down: int = 65433
KP_End: int = 65436
KP_Enter: int = 65421
KP_Equal: int = 65469
KP_F1: int = 65425
KP_F2: int = 65426
KP_F3: int = 65427
KP_F4: int = 65428
KP_Home: int = 65429
KP_Insert: int = 65438
KP_Left: int = 65430
KP_Multiply: int = 65450
KP_Next: int = 65435
KP_Page_Down: int = 65435
KP_Page_Up: int = 65434
KP_Prior: int = 65434
KP_Right: int = 65432
KP_Separator: int = 65452
KP_Space: int = 65408
KP_Subtract: int = 65453
KP_Tab: int = 65417
KP_Up: int = 65431
Kana_Lock: int = 65325
Kana_Shift: int = 65326
Kanji: int = 65313
Kanji_Bangou: int = 65335
Katakana: int = 65318
Kcedilla: int = 979
Korean_Won: int = 3839
L: int = 76
L1: int = 65480
L10: int = 65489
L2: int = 65481
L3: int = 65482
L4: int = 65483
L5: int = 65484
L6: int = 65485
L7: int = 65486
L8: int = 65487
L9: int = 65488
Lacute: int = 453
Last_Virtual_Screen: int = 65236
Lbelowdot: int = 16784950
Lcaron: int = 421
Lcedilla: int = 934
Left: int = 65361
Linefeed: int = 65290
LiraSign: int = 16785572
Lstroke: int = 419
M: int = 77
MAJOR_VERSION: int = 1
MAX_COMPOSE_LEN: int = 255
MICRO_VERSION: int = 30
MINOR_VERSION: int = 5
Mabovedot: int = 16784960
Macedonia_DSE: int = 1717
Macedonia_GJE: int = 1714
Macedonia_KJE: int = 1724
Macedonia_dse: int = 1701
Macedonia_gje: int = 1698
Macedonia_kje: int = 1708
Mae_Koho: int = 65342
Massyo: int = 65324
Menu: int = 65383
Meta_L: int = 65511
Meta_R: int = 65512
MillSign: int = 16785573
Mode_switch: int = 65406
MouseKeys_Accel_Enable: int = 65143
MouseKeys_Enable: int = 65142
Muhenkan: int = 65314
Multi_key: int = 65312
MultipleCandidate: int = 65341
N: int = 78
Nacute: int = 465
NairaSign: int = 16785574
Ncaron: int = 466
Ncedilla: int = 977
NewSheqelSign: int = 16785578
Next: int = 65366
Next_Virtual_Screen: int = 65234
Ntilde: int = 209
Num_Lock: int = 65407
O: int = 79
OE: int = 5052
Oacute: int = 211
Obarred: int = 16777631
Obelowdot: int = 16785100
Ocaron: int = 16777681
Ocircumflex: int = 212
Ocircumflexacute: int = 16785104
Ocircumflexbelowdot: int = 16785112
Ocircumflexgrave: int = 16785106
Ocircumflexhook: int = 16785108
Ocircumflextilde: int = 16785110
Odiaeresis: int = 214
Odoubleacute: int = 469
Ograve: int = 210
Ohook: int = 16785102
Ohorn: int = 16777632
Ohornacute: int = 16785114
Ohornbelowdot: int = 16785122
Ohorngrave: int = 16785116
Ohornhook: int = 16785118
Ohorntilde: int = 16785120
Omacron: int = 978
Ooblique: int = 216
Oslash: int = 216
Otilde: int = 213
Overlay1_Enable: int = 65144
Overlay2_Enable: int = 65145
P: int = 80
PATH_CONFIG: str = "/org/freedesktop/IBus/Config"
PATH_FACTORY: str = "/org/freedesktop/IBus/Factory"
PATH_IBUS: str = "/org/freedesktop/IBus"
PATH_INPUT_CONTEXT: str = "/org/freedesktop/IBus/InputContext_%d"
PATH_NOTIFICATIONS: str = "/org/freedesktop/IBus/Notifications"
PATH_PANEL: str = "/org/freedesktop/IBus/Panel"
PATH_PANEL_EXTENSION_EMOJI: str = "/org/freedesktop/IBus/Panel/Extension/Emoji"
Pabovedot: int = 16784982
Page_Down: int = 65366
Page_Up: int = 65365
Pause: int = 65299
PesetaSign: int = 16785575
Pointer_Accelerate: int = 65274
Pointer_Button1: int = 65257
Pointer_Button2: int = 65258
Pointer_Button3: int = 65259
Pointer_Button4: int = 65260
Pointer_Button5: int = 65261
Pointer_Button_Dflt: int = 65256
Pointer_DblClick1: int = 65263
Pointer_DblClick2: int = 65264
Pointer_DblClick3: int = 65265
Pointer_DblClick4: int = 65266
Pointer_DblClick5: int = 65267
Pointer_DblClick_Dflt: int = 65262
Pointer_DfltBtnNext: int = 65275
Pointer_DfltBtnPrev: int = 65276
Pointer_Down: int = 65251
Pointer_DownLeft: int = 65254
Pointer_DownRight: int = 65255
Pointer_Drag1: int = 65269
Pointer_Drag2: int = 65270
Pointer_Drag3: int = 65271
Pointer_Drag4: int = 65272
Pointer_Drag5: int = 65277
Pointer_Drag_Dflt: int = 65268
Pointer_EnableKeys: int = 65273
Pointer_Left: int = 65248
Pointer_Right: int = 65249
Pointer_Up: int = 65250
Pointer_UpLeft: int = 65252
Pointer_UpRight: int = 65253
Prev_Virtual_Screen: int = 65233
PreviousCandidate: int = 65342
Print: int = 65377
Prior: int = 65365
Q: int = 81
R: int = 82
R1: int = 65490
R10: int = 65499
R11: int = 65500
R12: int = 65501
R13: int = 65502
R14: int = 65503
R15: int = 65504
R2: int = 65491
R3: int = 65492
R4: int = 65493
R5: int = 65494
R6: int = 65495
R7: int = 65496
R8: int = 65497
R9: int = 65498
Racute: int = 448
Rcaron: int = 472
Rcedilla: int = 931
Redo: int = 65382
RepeatKeys_Enable: int = 65138
Return: int = 65293
Right: int = 65363
Romaji: int = 65316
RupeeSign: int = 16785576
S: int = 83
SCHWA: int = 16777615
SERVICE_CONFIG: str = "org.freedesktop.IBus.Config"
SERVICE_IBUS: str = "org.freedesktop.IBus"
SERVICE_NOTIFICATIONS: str = "org.freedesktop.IBus.Notifications"
SERVICE_PANEL: str = "org.freedesktop.IBus.Panel"
SERVICE_PANEL_EXTENSION: str = "org.freedesktop.IBus.Panel.Extension"
SERVICE_PANEL_EXTENSION_EMOJI: str = "org.freedesktop.IBus.Panel.Extension.Emoji"
SERVICE_PORTAL: str = "org.freedesktop.portal.IBus"
Sabovedot: int = 16784992
Sacute: int = 422
Scaron: int = 425
Scedilla: int = 426
Scircumflex: int = 734
Scroll_Lock: int = 65300
Select: int = 65376
Serbian_DJE: int = 1713
Serbian_DZE: int = 1727
Serbian_JE: int = 1720
Serbian_LJE: int = 1721
Serbian_NJE: int = 1722
Serbian_TSHE: int = 1723
Serbian_dje: int = 1697
Serbian_dze: int = 1711
Serbian_je: int = 1704
Serbian_lje: int = 1705
Serbian_nje: int = 1706
Serbian_tshe: int = 1707
Shift_L: int = 65505
Shift_Lock: int = 65510
Shift_R: int = 65506
SingleCandidate: int = 65340
SlowKeys_Enable: int = 65139
StickyKeys_Enable: int = 65141
Super_L: int = 65515
Super_R: int = 65516
Sys_Req: int = 65301
T: int = 84
THORN: int = 222
Tab: int = 65289
Tabovedot: int = 16785002
Tcaron: int = 427
Tcedilla: int = 478
Terminate_Server: int = 65237
Thai_baht: int = 3551
Thai_bobaimai: int = 3514
Thai_chochan: int = 3496
Thai_chochang: int = 3498
Thai_choching: int = 3497
Thai_chochoe: int = 3500
Thai_dochada: int = 3502
Thai_dodek: int = 3508
Thai_fofa: int = 3517
Thai_fofan: int = 3519
Thai_hohip: int = 3531
Thai_honokhuk: int = 3534
Thai_khokhai: int = 3490
Thai_khokhon: int = 3493
Thai_khokhuat: int = 3491
Thai_khokhwai: int = 3492
Thai_khorakhang: int = 3494
Thai_kokai: int = 3489
Thai_lakkhangyao: int = 3557
Thai_lekchet: int = 3575
Thai_lekha: int = 3573
Thai_lekhok: int = 3574
Thai_lekkao: int = 3577
Thai_leknung: int = 3569
Thai_lekpaet: int = 3576
Thai_leksam: int = 3571
Thai_leksi: int = 3572
Thai_leksong: int = 3570
Thai_leksun: int = 3568
Thai_lochula: int = 3532
Thai_loling: int = 3525
Thai_lu: int = 3526
Thai_maichattawa: int = 3563
Thai_maiek: int = 3560
Thai_maihanakat: int = 3537
Thai_maihanakat_maitho: int = 3550
Thai_maitaikhu: int = 3559
Thai_maitho: int = 3561
Thai_maitri: int = 3562
Thai_maiyamok: int = 3558
Thai_moma: int = 3521
Thai_ngongu: int = 3495
Thai_nikhahit: int = 3565
Thai_nonen: int = 3507
Thai_nonu: int = 3513
Thai_oang: int = 3533
Thai_paiyannoi: int = 3535
Thai_phinthu: int = 3546
Thai_phophan: int = 3518
Thai_phophung: int = 3516
Thai_phosamphao: int = 3520
Thai_popla: int = 3515
Thai_rorua: int = 3523
Thai_ru: int = 3524
Thai_saraa: int = 3536
Thai_saraaa: int = 3538
Thai_saraae: int = 3553
Thai_saraaimaimalai: int = 3556
Thai_saraaimaimuan: int = 3555
Thai_saraam: int = 3539
Thai_sarae: int = 3552
Thai_sarai: int = 3540
Thai_saraii: int = 3541
Thai_sarao: int = 3554
Thai_sarau: int = 3544
Thai_saraue: int = 3542
Thai_sarauee: int = 3543
Thai_sarauu: int = 3545
Thai_sorusi: int = 3529
Thai_sosala: int = 3528
Thai_soso: int = 3499
Thai_sosua: int = 3530
Thai_thanthakhat: int = 3564
Thai_thonangmontho: int = 3505
Thai_thophuthao: int = 3506
Thai_thothahan: int = 3511
Thai_thothan: int = 3504
Thai_thothong: int = 3512
Thai_thothung: int = 3510
Thai_topatak: int = 3503
Thai_totao: int = 3509
Thai_wowaen: int = 3527
Thai_yoyak: int = 3522
Thai_yoying: int = 3501
Thorn: int = 222
Touroku: int = 65323
Tslash: int = 940
U: int = 85
Uacute: int = 218
Ubelowdot: int = 16785124
Ubreve: int = 733
Ucircumflex: int = 219
Udiaeresis: int = 220
Udoubleacute: int = 475
Ugrave: int = 217
Uhook: int = 16785126
Uhorn: int = 16777647
Uhornacute: int = 16785128
Uhornbelowdot: int = 16785136
Uhorngrave: int = 16785130
Uhornhook: int = 16785132
Uhorntilde: int = 16785134
Ukrainian_GHE_WITH_UPTURN: int = 1725
Ukrainian_I: int = 1718
Ukrainian_IE: int = 1716
Ukrainian_YI: int = 1719
Ukrainian_ghe_with_upturn: int = 1709
Ukrainian_i: int = 1702
Ukrainian_ie: int = 1700
Ukrainian_yi: int = 1703
Ukranian_I: int = 1718
Ukranian_JE: int = 1716
Ukranian_YI: int = 1719
Ukranian_i: int = 1702
Ukranian_je: int = 1700
Ukranian_yi: int = 1703
Umacron: int = 990
Undo: int = 65381
Uogonek: int = 985
Up: int = 65362
Uring: int = 473
Utilde: int = 989
V: int = 86
VoidSymbol: int = 16777215
W: int = 87
Wacute: int = 16785026
Wcircumflex: int = 16777588
Wdiaeresis: int = 16785028
Wgrave: int = 16785024
WonSign: int = 16785577
X: int = 88
Xabovedot: int = 16785034
Y: int = 89
Yacute: int = 221
Ybelowdot: int = 16785140
Ycircumflex: int = 16777590
Ydiaeresis: int = 5054
Ygrave: int = 16785138
Yhook: int = 16785142
Ytilde: int = 16785144
Z: int = 90
Zabovedot: int = 431
Zacute: int = 428
Zcaron: int = 430
Zen_Koho: int = 65341
Zenkaku: int = 65320
Zenkaku_Hankaku: int = 65322
Zstroke: int = 16777653
_introspection_module = ...  # FIXME Constant
_lock = ...  # FIXME Constant
_namespace: str = "IBus"
_overrides_module = ...  # FIXME Constant
_version: str = "1.0"
a: int = 97
aacute: int = 225
abelowdot: int = 16785057
abovedot: int = 511
abreve: int = 483
abreveacute: int = 16785071
abrevebelowdot: int = 16785079
abrevegrave: int = 16785073
abrevehook: int = 16785075
abrevetilde: int = 16785077
acircumflex: int = 226
acircumflexacute: int = 16785061
acircumflexbelowdot: int = 16785069
acircumflexgrave: int = 16785063
acircumflexhook: int = 16785065
acircumflextilde: int = 16785067
acute: int = 180
adiaeresis: int = 228
ae: int = 230
agrave: int = 224
ahook: int = 16785059
amacron: int = 992
ampersand: int = 38
aogonek: int = 433
apostrophe: int = 39
approxeq: int = 16785992
approximate: int = 2248
aring: int = 229
asciicircum: int = 94
asciitilde: int = 126
asterisk: int = 42
at: int = 64
atilde: int = 227
b: int = 98
babovedot: int = 16784899
backslash: int = 92
ballotcross: int = 2804
bar: int = 124
because: int = 16785973
blank: int = 2527
botintegral: int = 2213
botleftparens: int = 2220
botleftsqbracket: int = 2216
botleftsummation: int = 2226
botrightparens: int = 2222
botrightsqbracket: int = 2218
botrightsummation: int = 2230
bott: int = 2550
botvertsummationconnector: int = 2228
braceleft: int = 123
braceright: int = 125
bracketleft: int = 91
bracketright: int = 93
braille_blank: int = 16787456
braille_dot_1: int = 65521
braille_dot_10: int = 65530
braille_dot_2: int = 65522
braille_dot_3: int = 65523
braille_dot_4: int = 65524
braille_dot_5: int = 65525
braille_dot_6: int = 65526
braille_dot_7: int = 65527
braille_dot_8: int = 65528
braille_dot_9: int = 65529
braille_dots_1: int = 16787457
braille_dots_12: int = 16787459
braille_dots_123: int = 16787463
braille_dots_1234: int = 16787471
braille_dots_12345: int = 16787487
braille_dots_123456: int = 16787519
braille_dots_1234567: int = 16787583
braille_dots_12345678: int = 16787711
braille_dots_1234568: int = 16787647
braille_dots_123457: int = 16787551
braille_dots_1234578: int = 16787679
braille_dots_123458: int = 16787615
braille_dots_12346: int = 16787503
braille_dots_123467: int = 16787567
braille_dots_1234678: int = 16787695
braille_dots_123468: int = 16787631
braille_dots_12347: int = 16787535
braille_dots_123478: int = 16787663
braille_dots_12348: int = 16787599
braille_dots_1235: int = 16787479
braille_dots_12356: int = 16787511
braille_dots_123567: int = 16787575
braille_dots_1235678: int = 16787703
braille_dots_123568: int = 16787639
braille_dots_12357: int = 16787543
braille_dots_123578: int = 16787671
braille_dots_12358: int = 16787607
braille_dots_1236: int = 16787495
braille_dots_12367: int = 16787559
braille_dots_123678: int = 16787687
braille_dots_12368: int = 16787623
braille_dots_1237: int = 16787527
braille_dots_12378: int = 16787655
braille_dots_1238: int = 16787591
braille_dots_124: int = 16787467
braille_dots_1245: int = 16787483
braille_dots_12456: int = 16787515
braille_dots_124567: int = 16787579
braille_dots_1245678: int = 16787707
braille_dots_124568: int = 16787643
braille_dots_12457: int = 16787547
braille_dots_124578: int = 16787675
braille_dots_12458: int = 16787611
braille_dots_1246: int = 16787499
braille_dots_12467: int = 16787563
braille_dots_124678: int = 16787691
braille_dots_12468: int = 16787627
braille_dots_1247: int = 16787531
braille_dots_12478: int = 16787659
braille_dots_1248: int = 16787595
braille_dots_125: int = 16787475
braille_dots_1256: int = 16787507
braille_dots_12567: int = 16787571
braille_dots_125678: int = 16787699
braille_dots_12568: int = 16787635
braille_dots_1257: int = 16787539
braille_dots_12578: int = 16787667
braille_dots_1258: int = 16787603
braille_dots_126: int = 16787491
braille_dots_1267: int = 16787555
braille_dots_12678: int = 16787683
braille_dots_1268: int = 16787619
braille_dots_127: int = 16787523
braille_dots_1278: int = 16787651
braille_dots_128: int = 16787587
braille_dots_13: int = 16787461
braille_dots_134: int = 16787469
braille_dots_1345: int = 16787485
braille_dots_13456: int = 16787517
braille_dots_134567: int = 16787581
braille_dots_1345678: int = 16787709
braille_dots_134568: int = 16787645
braille_dots_13457: int = 16787549
braille_dots_134578: int = 16787677
braille_dots_13458: int = 16787613
braille_dots_1346: int = 16787501
braille_dots_13467: int = 16787565
braille_dots_134678: int = 16787693
braille_dots_13468: int = 16787629
braille_dots_1347: int = 16787533
braille_dots_13478: int = 16787661
braille_dots_1348: int = 16787597
braille_dots_135: int = 16787477
braille_dots_1356: int = 16787509
braille_dots_13567: int = 16787573
braille_dots_135678: int = 16787701
braille_dots_13568: int = 16787637
braille_dots_1357: int = 16787541
braille_dots_13578: int = 16787669
braille_dots_1358: int = 16787605
braille_dots_136: int = 16787493
braille_dots_1367: int = 16787557
braille_dots_13678: int = 16787685
braille_dots_1368: int = 16787621
braille_dots_137: int = 16787525
braille_dots_1378: int = 16787653
braille_dots_138: int = 16787589
braille_dots_14: int = 16787465
braille_dots_145: int = 16787481
braille_dots_1456: int = 16787513
braille_dots_14567: int = 16787577
braille_dots_145678: int = 16787705
braille_dots_14568: int = 16787641
braille_dots_1457: int = 16787545
braille_dots_14578: int = 16787673
braille_dots_1458: int = 16787609
braille_dots_146: int = 16787497
braille_dots_1467: int = 16787561
braille_dots_14678: int = 16787689
braille_dots_1468: int = 16787625
braille_dots_147: int = 16787529
braille_dots_1478: int = 16787657
braille_dots_148: int = 16787593
braille_dots_15: int = 16787473
braille_dots_156: int = 16787505
braille_dots_1567: int = 16787569
braille_dots_15678: int = 16787697
braille_dots_1568: int = 16787633
braille_dots_157: int = 16787537
braille_dots_1578: int = 16787665
braille_dots_158: int = 16787601
braille_dots_16: int = 16787489
braille_dots_167: int = 16787553
braille_dots_1678: int = 16787681
braille_dots_168: int = 16787617
braille_dots_17: int = 16787521
braille_dots_178: int = 16787649
braille_dots_18: int = 16787585
braille_dots_2: int = 16787458
braille_dots_23: int = 16787462
braille_dots_234: int = 16787470
braille_dots_2345: int = 16787486
braille_dots_23456: int = 16787518
braille_dots_234567: int = 16787582
braille_dots_2345678: int = 16787710
braille_dots_234568: int = 16787646
braille_dots_23457: int = 16787550
braille_dots_234578: int = 16787678
braille_dots_23458: int = 16787614
braille_dots_2346: int = 16787502
braille_dots_23467: int = 16787566
braille_dots_234678: int = 16787694
braille_dots_23468: int = 16787630
braille_dots_2347: int = 16787534
braille_dots_23478: int = 16787662
braille_dots_2348: int = 16787598
braille_dots_235: int = 16787478
braille_dots_2356: int = 16787510
braille_dots_23567: int = 16787574
braille_dots_235678: int = 16787702
braille_dots_23568: int = 16787638
braille_dots_2357: int = 16787542
braille_dots_23578: int = 16787670
braille_dots_2358: int = 16787606
braille_dots_236: int = 16787494
braille_dots_2367: int = 16787558
braille_dots_23678: int = 16787686
braille_dots_2368: int = 16787622
braille_dots_237: int = 16787526
braille_dots_2378: int = 16787654
braille_dots_238: int = 16787590
braille_dots_24: int = 16787466
braille_dots_245: int = 16787482
braille_dots_2456: int = 16787514
braille_dots_24567: int = 16787578
braille_dots_245678: int = 16787706
braille_dots_24568: int = 16787642
braille_dots_2457: int = 16787546
braille_dots_24578: int = 16787674
braille_dots_2458: int = 16787610
braille_dots_246: int = 16787498
braille_dots_2467: int = 16787562
braille_dots_24678: int = 16787690
braille_dots_2468: int = 16787626
braille_dots_247: int = 16787530
braille_dots_2478: int = 16787658
braille_dots_248: int = 16787594
braille_dots_25: int = 16787474
braille_dots_256: int = 16787506
braille_dots_2567: int = 16787570
braille_dots_25678: int = 16787698
braille_dots_2568: int = 16787634
braille_dots_257: int = 16787538
braille_dots_2578: int = 16787666
braille_dots_258: int = 16787602
braille_dots_26: int = 16787490
braille_dots_267: int = 16787554
braille_dots_2678: int = 16787682
braille_dots_268: int = 16787618
braille_dots_27: int = 16787522
braille_dots_278: int = 16787650
braille_dots_28: int = 16787586
braille_dots_3: int = 16787460
braille_dots_34: int = 16787468
braille_dots_345: int = 16787484
braille_dots_3456: int = 16787516
braille_dots_34567: int = 16787580
braille_dots_345678: int = 16787708
braille_dots_34568: int = 16787644
braille_dots_3457: int = 16787548
braille_dots_34578: int = 16787676
braille_dots_3458: int = 16787612
braille_dots_346: int = 16787500
braille_dots_3467: int = 16787564
braille_dots_34678: int = 16787692
braille_dots_3468: int = 16787628
braille_dots_347: int = 16787532
braille_dots_3478: int = 16787660
braille_dots_348: int = 16787596
braille_dots_35: int = 16787476
braille_dots_356: int = 16787508
braille_dots_3567: int = 16787572
braille_dots_35678: int = 16787700
braille_dots_3568: int = 16787636
braille_dots_357: int = 16787540
braille_dots_3578: int = 16787668
braille_dots_358: int = 16787604
braille_dots_36: int = 16787492
braille_dots_367: int = 16787556
braille_dots_3678: int = 16787684
braille_dots_368: int = 16787620
braille_dots_37: int = 16787524
braille_dots_378: int = 16787652
braille_dots_38: int = 16787588
braille_dots_4: int = 16787464
braille_dots_45: int = 16787480
braille_dots_456: int = 16787512
braille_dots_4567: int = 16787576
braille_dots_45678: int = 16787704
braille_dots_4568: int = 16787640
braille_dots_457: int = 16787544
braille_dots_4578: int = 16787672
braille_dots_458: int = 16787608
braille_dots_46: int = 16787496
braille_dots_467: int = 16787560
braille_dots_4678: int = 16787688
braille_dots_468: int = 16787624
braille_dots_47: int = 16787528
braille_dots_478: int = 16787656
braille_dots_48: int = 16787592
braille_dots_5: int = 16787472
braille_dots_56: int = 16787504
braille_dots_567: int = 16787568
braille_dots_5678: int = 16787696
braille_dots_568: int = 16787632
braille_dots_57: int = 16787536
braille_dots_578: int = 16787664
braille_dots_58: int = 16787600
braille_dots_6: int = 16787488
braille_dots_67: int = 16787552
braille_dots_678: int = 16787680
braille_dots_68: int = 16787616
braille_dots_7: int = 16787520
braille_dots_78: int = 16787648
braille_dots_8: int = 16787584
breve: int = 418
brokenbar: int = 166
c: int = 99
cabovedot: int = 741
cacute: int = 486
careof: int = 2744
caret: int = 2812
caron: int = 439
ccaron: int = 488
ccedilla: int = 231
ccircumflex: int = 742
cedilla: int = 184
cent: int = 162
checkerboard: int = 2529
checkmark: int = 2803
circle: int = 3023
club: int = 2796
colon: int = 58
comma: int = 44
containsas: int = 16785931
copyright: int = 169
cr: int = 2532
crossinglines: int = 2542
cuberoot: int = 16785947
currency: int = 164
cursor: int = 2815
d: int = 100
dabovedot: int = 16784907
dagger: int = 2801
dcaron: int = 495
dead_abovecomma: int = 65124
dead_abovedot: int = 65110
dead_abovereversedcomma: int = 65125
dead_abovering: int = 65112
dead_acute: int = 65105
dead_belowbreve: int = 65131
dead_belowcircumflex: int = 65129
dead_belowdiaeresis: int = 65132
dead_belowdot: int = 65120
dead_belowmacron: int = 65128
dead_belowring: int = 65127
dead_belowtilde: int = 65130
dead_breve: int = 65109
dead_caron: int = 65114
dead_cedilla: int = 65115
dead_circumflex: int = 65106
dead_dasia: int = 65125
dead_diaeresis: int = 65111
dead_doubleacute: int = 65113
dead_grave: int = 65104
dead_hook: int = 65121
dead_horn: int = 65122
dead_iota: int = 65117
dead_macron: int = 65108
dead_ogonek: int = 65116
dead_perispomeni: int = 65107
dead_psili: int = 65124
dead_semivoiced_sound: int = 65119
dead_stroke: int = 65123
dead_tilde: int = 65107
dead_voiced_sound: int = 65118
decimalpoint: int = 2749
degree: int = 176
diaeresis: int = 168
diamond: int = 2797
digitspace: int = 2725
dintegral: int = 16785964
division: int = 247
dollar: int = 36
doubbaselinedot: int = 2735
doubleacute: int = 445
doubledagger: int = 2802
doublelowquotemark: int = 2814
downarrow: int = 2302
downcaret: int = 2984
downshoe: int = 3030
downstile: int = 3012
downtack: int = 3010
dstroke: int = 496
e: int = 101
eabovedot: int = 1004
eacute: int = 233
ebelowdot: int = 16785081
ecaron: int = 492
ecircumflex: int = 234
ecircumflexacute: int = 16785087
ecircumflexbelowdot: int = 16785095
ecircumflexgrave: int = 16785089
ecircumflexhook: int = 16785091
ecircumflextilde: int = 16785093
ediaeresis: int = 235
egrave: int = 232
ehook: int = 16785083
eightsubscript: int = 16785544
eightsuperior: int = 16785528
elementof: int = 16785928
ellipsis: int = 2734
em3space: int = 2723
em4space: int = 2724
emacron: int = 954
emdash: int = 2729
emfilledcircle: int = 2782
emfilledrect: int = 2783
emopencircle: int = 2766
emopenrectangle: int = 2767
emptyset: int = 16785925
emspace: int = 2721
endash: int = 2730
enfilledcircbullet: int = 2790
enfilledsqbullet: int = 2791
eng: int = 959
enopencircbullet: int = 2784
enopensquarebullet: int = 2785
enspace: int = 2722
eogonek: int = 490
equal: int = 61
eth: int = 240
etilde: int = 16785085
exclam: int = 33
exclamdown: int = 161
f: int = 102
fabovedot: int = 16784927
femalesymbol: int = 2808
ff: int = 2531
figdash: int = 2747
filledlefttribullet: int = 2780
filledrectbullet: int = 2779
filledrighttribullet: int = 2781
filledtribulletdown: int = 2793
filledtribulletup: int = 2792
fiveeighths: int = 2757
fivesixths: int = 2743
fivesubscript: int = 16785541
fivesuperior: int = 16785525
fourfifths: int = 2741
foursubscript: int = 16785540
foursuperior: int = 16785524
fourthroot: int = 16785948
function: int = 2294
g: int = 103
gabovedot: int = 757
gbreve: int = 699
gcaron: int = 16777703
gcedilla: int = 955
gcircumflex: int = 760
grave: int = 96
greater: int = 62
greaterthanequal: int = 2238
guillemotleft: int = 171
guillemotright: int = 187
h: int = 104
hairspace: int = 2728
hcircumflex: int = 694
heart: int = 2798
hebrew_aleph: int = 3296
hebrew_ayin: int = 3314
hebrew_bet: int = 3297
hebrew_beth: int = 3297
hebrew_chet: int = 3303
hebrew_dalet: int = 3299
hebrew_daleth: int = 3299
hebrew_doublelowline: int = 3295
hebrew_finalkaph: int = 3306
hebrew_finalmem: int = 3309
hebrew_finalnun: int = 3311
hebrew_finalpe: int = 3315
hebrew_finalzade: int = 3317
hebrew_finalzadi: int = 3317
hebrew_gimel: int = 3298
hebrew_gimmel: int = 3298
hebrew_he: int = 3300
hebrew_het: int = 3303
hebrew_kaph: int = 3307
hebrew_kuf: int = 3319
hebrew_lamed: int = 3308
hebrew_mem: int = 3310
hebrew_nun: int = 3312
hebrew_pe: int = 3316
hebrew_qoph: int = 3319
hebrew_resh: int = 3320
hebrew_samech: int = 3313
hebrew_samekh: int = 3313
hebrew_shin: int = 3321
hebrew_taf: int = 3322
hebrew_taw: int = 3322
hebrew_tet: int = 3304
hebrew_teth: int = 3304
hebrew_waw: int = 3301
hebrew_yod: int = 3305
hebrew_zade: int = 3318
hebrew_zadi: int = 3318
hebrew_zain: int = 3302
hebrew_zayin: int = 3302
hexagram: int = 2778
horizconnector: int = 2211
horizlinescan1: int = 2543
horizlinescan3: int = 2544
horizlinescan5: int = 2545
horizlinescan7: int = 2546
horizlinescan9: int = 2547
hstroke: int = 689
ht: int = 2530
hyphen: int = 173
i: int = 105
iacute: int = 237
ibelowdot: int = 16785099
ibreve: int = 16777517
icircumflex: int = 238
identical: int = 2255
idiaeresis: int = 239
idotless: int = 697
ifonlyif: int = 2253
igrave: int = 236
ihook: int = 16785097
imacron: int = 1007
implies: int = 2254
includedin: int = 2266
includes: int = 2267
infinity: int = 2242
integral: int = 2239
intersection: int = 2268
iogonek: int = 999
itilde: int = 949
j: int = 106
jcircumflex: int = 700
jot: int = 3018
k: int = 107
kana_A: int = 1201
kana_CHI: int = 1217
kana_E: int = 1204
kana_FU: int = 1228
kana_HA: int = 1226
kana_HE: int = 1229
kana_HI: int = 1227
kana_HO: int = 1230
kana_HU: int = 1228
kana_I: int = 1202
kana_KA: int = 1206
kana_KE: int = 1209
kana_KI: int = 1207
kana_KO: int = 1210
kana_KU: int = 1208
kana_MA: int = 1231
kana_ME: int = 1234
kana_MI: int = 1232
kana_MO: int = 1235
kana_MU: int = 1233
kana_N: int = 1245
kana_NA: int = 1221
kana_NE: int = 1224
kana_NI: int = 1222
kana_NO: int = 1225
kana_NU: int = 1223
kana_O: int = 1205
kana_RA: int = 1239
kana_RE: int = 1242
kana_RI: int = 1240
kana_RO: int = 1243
kana_RU: int = 1241
kana_SA: int = 1211
kana_SE: int = 1214
kana_SHI: int = 1212
kana_SO: int = 1215
kana_SU: int = 1213
kana_TA: int = 1216
kana_TE: int = 1219
kana_TI: int = 1217
kana_TO: int = 1220
kana_TSU: int = 1218
kana_TU: int = 1218
kana_U: int = 1203
kana_WA: int = 1244
kana_WO: int = 1190
kana_YA: int = 1236
kana_YO: int = 1238
kana_YU: int = 1237
kana_a: int = 1191
kana_closingbracket: int = 1187
kana_comma: int = 1188
kana_conjunctive: int = 1189
kana_e: int = 1194
kana_fullstop: int = 1185
kana_i: int = 1192
kana_middledot: int = 1189
kana_o: int = 1195
kana_openingbracket: int = 1186
kana_switch: int = 65406
kana_tsu: int = 1199
kana_tu: int = 1199
kana_u: int = 1193
kana_ya: int = 1196
kana_yo: int = 1198
kana_yu: int = 1197
kappa: int = 930
kcedilla: int = 1011
kra: int = 930
l: int = 108
lacute: int = 485
latincross: int = 2777
lbelowdot: int = 16784951
lcaron: int = 437
lcedilla: int = 950
leftanglebracket: int = 2748
leftarrow: int = 2299
leftcaret: int = 2979
leftdoublequotemark: int = 2770
leftmiddlecurlybrace: int = 2223
leftopentriangle: int = 2764
leftpointer: int = 2794
leftradical: int = 2209
leftshoe: int = 3034
leftsinglequotemark: int = 2768
leftt: int = 2548
lefttack: int = 3036
less: int = 60
lessthanequal: int = 2236
lf: int = 2533
logicaland: int = 2270
logicalor: int = 2271
lowleftcorner: int = 2541
lowrightcorner: int = 2538
lstroke: int = 435
m: int = 109
mabovedot: int = 16784961
macron: int = 175
malesymbol: int = 2807
maltesecross: int = 2800
marker: int = 2751
masculine: int = 186
minus: int = 45
minutes: int = 2774
mu: int = 181
multiply: int = 215
musicalflat: int = 2806
musicalsharp: int = 2805
n: int = 110
nabla: int = 2245
nacute: int = 497
ncaron: int = 498
ncedilla: int = 1009
ninesubscript: int = 16785545
ninesuperior: int = 16785529
nl: int = 2536
nobreakspace: int = 160
notapproxeq: int = 16785991
notelementof: int = 16785929
notequal: int = 2237
notidentical: int = 16786018
notsign: int = 172
ntilde: int = 241
numbersign: int = 35
numerosign: int = 1712
o: int = 111
oacute: int = 243
obarred: int = 16777845
obelowdot: int = 16785101
ocaron: int = 16777682
ocircumflex: int = 244
ocircumflexacute: int = 16785105
ocircumflexbelowdot: int = 16785113
ocircumflexgrave: int = 16785107
ocircumflexhook: int = 16785109
ocircumflextilde: int = 16785111
odiaeresis: int = 246
odoubleacute: int = 501
oe: int = 5053
ogonek: int = 434
ograve: int = 242
ohook: int = 16785103
ohorn: int = 16777633
ohornacute: int = 16785115
ohornbelowdot: int = 16785123
ohorngrave: int = 16785117
ohornhook: int = 16785119
ohorntilde: int = 16785121
omacron: int = 1010
oneeighth: int = 2755
onefifth: int = 2738
onehalf: int = 189
onequarter: int = 188
onesixth: int = 2742
onesubscript: int = 16785537
onesuperior: int = 185
onethird: int = 2736
ooblique: int = 248
openrectbullet: int = 2786
openstar: int = 2789
opentribulletdown: int = 2788
opentribulletup: int = 2787
ordfeminine: int = 170
oslash: int = 248
otilde: int = 245
overbar: int = 3008
overline: int = 1150
p: int = 112
pabovedot: int = 16784983
paragraph: int = 182
parenleft: int = 40
parenright: int = 41
partdifferential: int = 16785922
partialderivative: int = 2287
percent: int = 37
period: int = 46
periodcentered: int = 183
phonographcopyright: int = 2811
plus: int = 43
plusminus: int = 177
prescription: int = 2772
prolongedsound: int = 1200
punctspace: int = 2726
q: int = 113
quad: int = 3020
question: int = 63
questiondown: int = 191
quotedbl: int = 34
quoteleft: int = 96
quoteright: int = 39
r: int = 114
racute: int = 480
radical: int = 2262
rcaron: int = 504
rcedilla: int = 947
registered: int = 174
rightanglebracket: int = 2750
rightarrow: int = 2301
rightcaret: int = 2982
rightdoublequotemark: int = 2771
rightmiddlecurlybrace: int = 2224
rightmiddlesummation: int = 2231
rightopentriangle: int = 2765
rightpointer: int = 2795
rightshoe: int = 3032
rightsinglequotemark: int = 2769
rightt: int = 2549
righttack: int = 3068
s: int = 115
sabovedot: int = 16784993
sacute: int = 438
scaron: int = 441
scedilla: int = 442
schwa: int = 16777817
scircumflex: int = 766
script_switch: int = 65406
seconds: int = 2775
section: int = 167
semicolon: int = 59
semivoicedsound: int = 1247
seveneighths: int = 2758
sevensubscript: int = 16785543
sevensuperior: int = 16785527
signaturemark: int = 2762
signifblank: int = 2732
similarequal: int = 2249
singlelowquotemark: int = 2813
sixsubscript: int = 16785542
sixsuperior: int = 16785526
slash: int = 47
soliddiamond: int = 2528
space: int = 32
squareroot: int = 16785946
ssharp: int = 223
sterling: int = 163
stricteq: int = 16786019
t: int = 116
tabovedot: int = 16785003
tcaron: int = 443
tcedilla: int = 510
telephone: int = 2809
telephonerecorder: int = 2810
therefore: int = 2240
thinspace: int = 2727
thorn: int = 254
threeeighths: int = 2756
threefifths: int = 2740
threequarters: int = 190
threesubscript: int = 16785539
threesuperior: int = 179
tintegral: int = 16785965
topintegral: int = 2212
topleftparens: int = 2219
topleftradical: int = 2210
topleftsqbracket: int = 2215
topleftsummation: int = 2225
toprightparens: int = 2221
toprightsqbracket: int = 2217
toprightsummation: int = 2229
topt: int = 2551
topvertsummationconnector: int = 2227
trademark: int = 2761
trademarkincircle: int = 2763
tslash: int = 956
twofifths: int = 2739
twosubscript: int = 16785538
twosuperior: int = 178
twothirds: int = 2737
u: int = 117
uacute: int = 250
ubelowdot: int = 16785125
ubreve: int = 765
ucircumflex: int = 251
udiaeresis: int = 252
udoubleacute: int = 507
ugrave: int = 249
uhook: int = 16785127
uhorn: int = 16777648
uhornacute: int = 16785129
uhornbelowdot: int = 16785137
uhorngrave: int = 16785131
uhornhook: int = 16785133
uhorntilde: int = 16785135
umacron: int = 1022
underbar: int = 3014
underscore: int = 95
union: int = 2269
uogonek: int = 1017
uparrow: int = 2300
upcaret: int = 2985
upleftcorner: int = 2540
uprightcorner: int = 2539
upshoe: int = 3011
upstile: int = 3027
uptack: int = 3022
uring: int = 505
utilde: int = 1021
v: int = 118
variation: int = 2241
vertbar: int = 2552
vertconnector: int = 2214
voicedsound: int = 1246
vt: int = 2537
w: int = 119
wacute: int = 16785027
wcircumflex: int = 16777589
wdiaeresis: int = 16785029
wgrave: int = 16785025
x: int = 120
xabovedot: int = 16785035
y: int = 121
yacute: int = 253
ybelowdot: int = 16785141
ycircumflex: int = 16777591
ydiaeresis: int = 255
yen: int = 165
ygrave: int = 16785139
yhook: int = 16785143
ytilde: int = 16785145
z: int = 122
zabovedot: int = 447
zacute: int = 444
zcaron: int = 446
zerosubscript: int = 16785536
zerosuperior: int = 16785520
zstroke: int = 16777654

def accelerator_name(accelerator_key: int, accelerator_mods: ModifierType) -> str: ...
def accelerator_parse(accelerator: str) -> typing.Tuple[int, ModifierType]: ...
def accelerator_valid(keyval: int, modifiers: ModifierType) -> bool: ...
def attr_background_new(color: int, start_index: int, end_index: int) -> Attribute: ...
def attr_foreground_new(color: int, start_index: int, end_index: int) -> Attribute: ...
def attr_underline_new(
    underline_type: int, start_index: int, end_index: int
) -> Attribute: ...
def emoji_dict_load(path: str) -> dict[str, None]: ...
def emoji_dict_lookup(dict: dict[str, EmojiData], emoji: str) -> EmojiData: ...
def emoji_dict_save(path: str, dict: dict[str, None]) -> None: ...
def error_quark() -> int: ...
def free_strv(strv: str) -> None: ...
def get_address() -> str: ...
def get_daemon_uid() -> int: ...
def get_language_name(_locale: str) -> str: ...
def get_local_machine_id() -> str: ...
def get_socket_path() -> str: ...
def get_timeout() -> int: ...
def get_untranslated_language_name(_locale: str) -> str: ...
def get_user_name() -> str: ...
def init() -> None: ...
def key_event_from_string(string: str) -> typing.Tuple[bool, int, int]: ...
def key_event_to_string(keyval: int, modifiers: int) -> str: ...
def keyval_convert_case(symbol: int) -> typing.Tuple[int, int]: ...
def keyval_from_name(keyval_name: str) -> int: ...
def keyval_name(keyval: int) -> str: ...
def keyval_to_lower(keyval: int) -> int: ...
def keyval_to_unicode(keyval: int) -> str: ...
def keyval_to_upper(keyval: int) -> int: ...
def main() -> None: ...
def quit() -> None: ...
def set_display(display: str) -> None: ...
def set_log_handler(verbose: bool) -> None: ...
def unicode_to_keyval(wc: str) -> int: ...
def unset_log_handler() -> None: ...
def write_address(address: str) -> None: ...
def xml_parse_buffer(buffer: str) -> XML: ...
def xml_parse_file(name: str) -> XML: ...

class AttrList(Serializable):
    """
    :Constructors:

    ::

        AttrList(**properties)
        new() -> IBus.AttrList

    Object IBusAttrList

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable = ...
    attributes: list[None] = ...
    def append(self, attr: Attribute) -> None: ...
    def get(self, index: int) -> Attribute: ...
    @classmethod
    def new(cls) -> AttrList: ...

class AttrListClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AttrListClass()
    """

    parent: SerializableClass = ...

class Attribute(Serializable):
    """
    :Constructors:

    ::

        Attribute(**properties)
        new(type:int, value:int, start_index:int, end_index:int) -> IBus.Attribute

    Object IBusAttribute

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable = ...
    type: int = ...
    value: int = ...
    start_index: int = ...
    end_index: int = ...
    def get_attr_type(self) -> int: ...
    def get_end_index(self) -> int: ...
    def get_start_index(self) -> int: ...
    def get_value(self) -> int: ...
    @classmethod
    def new(
        cls, type: int, value: int, start_index: int, end_index: int
    ) -> Attribute: ...

class AttributeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AttributeClass()
    """

    parent: SerializableClass = ...

class Bus(Object):
    """
    :Constructors:

    ::

        Bus(**properties)
        new() -> IBus.Bus
        new_async() -> IBus.Bus
        new_async_client() -> IBus.Bus

    Object IBusBus

    Signals from IBusBus:
      connected ()
      disconnected ()
      global-engine-changed (gchararray)
      name-owner-changed (gchararray, gchararray, gchararray)
      global-shortcut-key-responded (guchar, gboolean, gboolean)

    Properties from IBusBus:
      connect-async -> gboolean: Connect Async
        Connect asynchronously to the bus
      client-only -> gboolean: ClientOnly
        Client use only

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        client_only: bool
        connect_async: bool

    props: Props = ...
    parent: Object = ...
    priv: BusPrivate = ...
    def __init__(self, client_only: bool = ..., connect_async: bool = ...) -> None: ...
    def add_match(self, rule: str) -> bool: ...
    def add_match_async(
        self,
        rule: str,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def add_match_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def create_input_context(self, client_name: str) -> InputContext: ...
    def create_input_context_async(
        self,
        client_name: str,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def create_input_context_async_finish(
        self, res: Gio.AsyncResult
    ) -> InputContext: ...
    def current_input_context(self) -> str: ...
    def current_input_context_async(
        self,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def current_input_context_async_finish(self, res: Gio.AsyncResult) -> str: ...
    def exit(self, restart: bool) -> bool: ...
    def exit_async(
        self,
        restart: bool,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def exit_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def get_config(self) -> Config: ...
    def get_connection(self) -> Gio.DBusConnection: ...
    def get_engines_by_names(self, names: typing.Sequence[str]) -> list[EngineDesc]: ...
    def get_global_engine(self) -> EngineDesc: ...
    def get_global_engine_async(
        self,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def get_global_engine_async_finish(self, res: Gio.AsyncResult) -> EngineDesc: ...
    def get_ibus_property(self, property_name: str) -> GLib.Variant: ...
    def get_ibus_property_async(
        self,
        property_name: str,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def get_ibus_property_async_finish(self, res: Gio.AsyncResult) -> GLib.Variant: ...
    def get_name_owner(self, name: str) -> str: ...
    def get_name_owner_async(
        self,
        name: str,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def get_name_owner_async_finish(self, res: Gio.AsyncResult) -> str: ...
    def get_service_name(self) -> str: ...
    def get_use_global_engine(self) -> bool: ...
    def get_use_global_engine_async(
        self,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def get_use_global_engine_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def get_use_sys_layout(self) -> bool: ...
    def get_use_sys_layout_async(
        self,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def get_use_sys_layout_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def hello(self) -> str: ...
    def is_connected(self) -> bool: ...
    def is_global_engine_enabled(self) -> bool: ...
    def is_global_engine_enabled_async(
        self,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def is_global_engine_enabled_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def list_active_engines(self) -> list[EngineDesc]: ...
    def list_active_engines_async(
        self,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def list_active_engines_async_finish(
        self, res: Gio.AsyncResult
    ) -> list[EngineDesc]: ...
    def list_engines(self) -> list[EngineDesc]: ...
    def list_engines_async(
        self,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def list_engines_async_finish(self, res: Gio.AsyncResult) -> list[EngineDesc]: ...
    def list_names(self) -> list[str]: ...
    def list_queued_owners(self, name: str) -> list[str]: ...
    def name_has_owner(self, name: str) -> bool: ...
    def name_has_owner_async(
        self,
        name: str,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def name_has_owner_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    @classmethod
    def new(cls) -> Bus: ...
    @classmethod
    def new_async(cls) -> Bus: ...
    @classmethod
    def new_async_client(cls) -> Bus: ...
    def preload_engines(self, names: typing.Sequence[str]) -> bool: ...
    def preload_engines_async(
        self,
        names: typing.Sequence[str],
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def preload_engines_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def register_component(self, component: Component) -> bool: ...
    def register_component_async(
        self,
        component: Component,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def register_component_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def release_name(self, name: str) -> int: ...
    def release_name_async(
        self,
        name: str,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def release_name_async_finish(self, res: Gio.AsyncResult) -> int: ...
    def remove_match(self, rule: str) -> bool: ...
    def remove_match_async(
        self,
        rule: str,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def remove_match_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def request_name(self, name: str, flags: int) -> int: ...
    def request_name_async(
        self,
        name: str,
        flags: int,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def request_name_async_finish(self, res: Gio.AsyncResult) -> int: ...
    def set_global_engine(self, global_engine: str) -> bool: ...
    def set_global_engine_async(
        self,
        global_engine: str,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def set_global_engine_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def set_global_shortcut_keys(
        self, gtype: BusGlobalBindingType, keys: typing.Sequence[ProcessKeyEventData]
    ) -> bool: ...
    def set_global_shortcut_keys_async(
        self,
        gtype: BusGlobalBindingType,
        keys: typing.Sequence[ProcessKeyEventData],
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def set_global_shortcut_keys_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def set_ibus_property(self, property_name: str, value: GLib.Variant) -> None: ...
    def set_ibus_property_async(
        self,
        property_name: str,
        value: GLib.Variant,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def set_ibus_property_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def set_watch_dbus_signal(self, watch: bool) -> None: ...
    def set_watch_ibus_signal(self, watch: bool) -> None: ...

class BusClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BusClass()
    """

    parent: ObjectClass = ...

class BusPrivate(GObject.GPointer): ...

class Component(Serializable):
    """
    :Constructors:

    ::

        Component(**properties)
        new(name:str, description:str, version:str, license:str, author:str, homepage:str, command_line:str, textdomain:str) -> IBus.Component
        new_from_file(filename:str) -> IBus.Component
        new_from_xml_node(node:IBus.XML) -> IBus.Component

    Object IBusComponent

    Properties from IBusComponent:
      name -> gchararray: component name
        The name of component
      description -> gchararray: component description
        The description of component
      version -> gchararray: component version
        The version of component
      license -> gchararray: component license
        The license of component
      author -> gchararray: component author
        The author of component
      homepage -> gchararray: component homepage
        The homepage of component
      command-line -> gchararray: component command-line
        The command line of component
      textdomain -> gchararray: component textdomain
        The textdomain path of component

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        author: str
        command_line: str
        description: str
        homepage: str
        license: str
        name: str
        textdomain: str
        version: str

    props: Props = ...
    parent: Serializable = ...
    priv: ComponentPrivate = ...
    pdummy: list[None] = ...
    def __init__(
        self,
        author: str = ...,
        command_line: str = ...,
        description: str = ...,
        homepage: str = ...,
        license: str = ...,
        name: str = ...,
        textdomain: str = ...,
        version: str = ...,
    ) -> None: ...
    def add_engine(self, engine=None, **kwargs): ...  # FIXME Function
    def add_observed_path(self, path: str, access_fs: bool) -> None: ...
    def check_modification(self) -> bool: ...
    def get_author(self) -> str: ...
    def get_description(self) -> str: ...
    def get_engines(self) -> list[EngineDesc]: ...
    def get_exec(self) -> str: ...
    def get_homepage(self) -> str: ...
    def get_license(self) -> str: ...
    def get_name(self) -> str: ...
    def get_observed_paths(self) -> list[ObservedPath]: ...
    def get_textdomain(self) -> str: ...
    def get_version(self) -> str: ...
    @classmethod
    def new(
        cls,
        name: str,
        description: str,
        version: str,
        license: str,
        author: str,
        homepage: str,
        command_line: str,
        textdomain: str,
    ) -> Component: ...
    @classmethod
    def new_from_file(cls, filename: str) -> Component: ...
    @classmethod
    def new_from_xml_node(cls, node: XML) -> Component: ...
    def output(self, output: GLib.String, indent: int) -> None: ...
    def output_engines(self, output: GLib.String, indent: int) -> None: ...

class ComponentClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ComponentClass()
    """

    parent: SerializableClass = ...

class ComponentPrivate(GObject.GPointer): ...

class Config(Proxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable):
    """
    :Constructors:

    ::

        Config(**properties)
        new(connection:Gio.DBusConnection, cancellable:Gio.Cancellable=None) -> IBus.Config
        new_async_finish(res:Gio.AsyncResult) -> IBus.Config

    Object IBusConfig

    Signals from IBusConfig:
      value-changed (gchararray, gchararray, GVariant)

    Signals from IBusProxy:
      destroy ()

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
      g-bus-type -> GBusType: g-bus-type
      g-name -> gchararray: g-name
      g-name-owner -> gchararray: g-name-owner
      g-flags -> GDBusProxyFlags: g-flags
      g-object-path -> gchararray: g-object-path
      g-interface-name -> gchararray: g-interface-name
      g-default-timeout -> gint: g-default-timeout
      g-interface-info -> GDBusInterfaceInfo: g-interface-info

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    props: Props = ...
    parent: Proxy = ...
    priv: ConfigPrivate = ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ) -> None: ...
    def get_value(self, section, name, default=None): ...  # FIXME Function
    def get_value_async(
        self,
        section: str,
        name: str,
        timeout_ms: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def get_value_async_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    def get_values(self, section: str) -> GLib.Variant: ...
    def get_values_async(
        self,
        section: str,
        timeout_ms: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def get_values_async_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    @classmethod
    def new(
        cls,
        connection: Gio.DBusConnection,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> Config: ...
    @staticmethod
    def new_async(
        connection: Gio.DBusConnection,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @classmethod
    def new_async_finish(cls, res: Gio.AsyncResult) -> Config: ...
    def set_value(self, section, name, value): ...  # FIXME Function
    def set_value_async(
        self,
        section: str,
        name: str,
        value: GLib.Variant,
        timeout_ms: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def set_value_async_finish(self, result: Gio.AsyncResult) -> bool: ...
    def unset(self, section: str, name: str) -> bool: ...
    def unwatch(
        self, section: typing.Optional[str] = None, name: typing.Optional[str] = None
    ) -> bool: ...
    def watch(
        self, section: typing.Optional[str] = None, name: typing.Optional[str] = None
    ) -> bool: ...

class ConfigClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ConfigClass()
    """

    parent: ProxyClass = ...

class ConfigPrivate(GObject.GPointer): ...

class ConfigService(Service):
    """
    :Constructors:

    ::

        ConfigService(**properties)
        new(connection:Gio.DBusConnection) -> IBus.ConfigService

    Object IBusConfigService

    Properties from IBusService:
      object-path -> gchararray: object path
        The path of service object
      connection -> GDBusConnection: connection
        The connection of service object

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        connection: Gio.DBusConnection
        object_path: str

    props: Props = ...
    parent: Service = ...
    def __init__(
        self, connection: Gio.DBusConnection = ..., object_path: str = ...
    ) -> None: ...
    def do_get_value(self, section: str, name: str) -> GLib.Variant: ...
    def do_get_values(self, section: str) -> GLib.Variant: ...
    def do_set_value(self, section: str, name: str, value: GLib.Variant) -> bool: ...
    def do_unset_value(self, section: str, name: str) -> bool: ...
    @classmethod
    def new(cls, connection: Gio.DBusConnection) -> ConfigService: ...
    def value_changed(self, section: str, name: str, value: GLib.Variant) -> None: ...

class ConfigServiceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ConfigServiceClass()
    """

    parent: ServiceClass = ...
    set_value: typing.Callable[[ConfigService, str, str, GLib.Variant], bool] = ...
    get_value: typing.Callable[[ConfigService, str, str], GLib.Variant] = ...
    unset_value: typing.Callable[[ConfigService, str, str], bool] = ...
    get_values: typing.Callable[[ConfigService, str], GLib.Variant] = ...
    pdummy: list[None] = ...

class EmojiData(Serializable):
    """
    :Constructors:

    ::

        EmojiData(**properties)

    Object IBusEmojiData

    Properties from IBusEmojiData:
      emoji -> gchararray: emoji character
        The emoji character UTF-8
      annotations -> gpointer: emoji annotations
        The emoji annotation list
      description -> gchararray: emoji description
        The emoji description
      category -> gchararray: emoji category
        The emoji category

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        annotations: None
        category: str
        description: str
        emoji: str

    props: Props = ...
    parent: Serializable = ...
    priv: EmojiDataPrivate = ...
    def __init__(
        self,
        annotations: None = ...,
        category: str = ...,
        description: str = ...,
        emoji: str = ...,
    ) -> None: ...
    def get_annotations(self) -> list[str]: ...
    def get_category(self) -> str: ...
    def get_description(self) -> str: ...
    def get_emoji(self) -> str: ...
    @staticmethod
    def load(path: str) -> list[EmojiData]: ...
    @staticmethod
    def save(path: str, list: list[EmojiData]) -> None: ...
    def set_annotations(self, annotations: list[str]) -> None: ...
    def set_description(self, description: str) -> None: ...

class EmojiDataClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EmojiDataClass()
    """

    parent: SerializableClass = ...

class EmojiDataPrivate(GObject.GPointer): ...

class Engine(Service):
    """
    :Constructors:

    ::

        Engine(**properties)
        new(engine_name:str, object_path:str, connection:Gio.DBusConnection) -> IBus.Engine
        new_with_type(engine_type:GType, engine_name:str, object_path:str, connection:Gio.DBusConnection) -> IBus.Engine

    Object IBusEngine

    Signals from IBusEngine:
      process-key-event (guint, guint, guint) -> gboolean
      focus-in ()
      focus-in-id (gchararray, gchararray)
      focus-out ()
      focus-out-id (gchararray)
      reset ()
      enable ()
      disable ()
      set-cursor-location (gint, gint, gint, gint)
      set-capabilities (guint)
      page-up ()
      page-down ()
      cursor-up ()
      cursor-down ()
      candidate-clicked (guint, guint, guint)
      property-activate (gchararray, guint)
      property-show (gchararray)
      property-hide (gchararray)
      process-hand-writing-event (gpointer, guint)
      cancel-hand-writing (guint)
      set-surrounding-text (GObject, guint, guint)
      set-content-type (guint, guint)

    Properties from IBusEngine:
      engine-name -> gchararray: engine name
        engine name
      has-focus-id -> gboolean: has focus id
        Has focus ID
      active-surrounding-text -> gboolean: enable surrounding text update by focus event
        Enable surrounding text update by focus event

    Properties from IBusService:
      object-path -> gchararray: object path
        The path of service object
      connection -> GDBusConnection: connection
        The connection of service object

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        active_surrounding_text: bool
        engine_name: str
        has_focus_id: bool
        connection: Gio.DBusConnection
        object_path: str

    props: Props = ...
    parent: Service = ...
    priv: EnginePrivate = ...
    enabled: bool = ...
    has_focus: bool = ...
    cursor_area: Rectangle = ...
    client_capabilities: int = ...
    def __init__(
        self,
        active_surrounding_text: bool = ...,
        engine_name: str = ...,
        has_focus_id: bool = ...,
        connection: Gio.DBusConnection = ...,
        object_path: str = ...,
    ) -> None: ...
    def commit_text(self, text: Text) -> None: ...
    def delete_surrounding_text(self, offset: int, nchars: int) -> None: ...
    def do_cancel_hand_writing(self, n_strokes: int) -> None: ...
    def do_candidate_clicked(self, index: int, button: int, state: int) -> None: ...
    def do_cursor_down(self) -> None: ...
    def do_cursor_up(self) -> None: ...
    def do_disable(self) -> None: ...
    def do_enable(self) -> None: ...
    def do_focus_in(self) -> None: ...
    def do_focus_in_id(self, object_path: str, client: str) -> None: ...
    def do_focus_out(self) -> None: ...
    def do_focus_out_id(self, object_path: str) -> None: ...
    def do_page_down(self) -> None: ...
    def do_page_up(self) -> None: ...
    def do_process_hand_writing_event(
        self, coordinates: float, coordinates_len: int
    ) -> None: ...
    def do_process_key_event(self, keyval: int, keycode: int, state: int) -> bool: ...
    def do_property_activate(self, prop_name: str, prop_state: int) -> None: ...
    def do_property_hide(self, prop_name: str) -> None: ...
    def do_property_show(self, prop_name: str) -> None: ...
    def do_reset(self) -> None: ...
    def do_set_capabilities(self, caps: int) -> None: ...
    def do_set_content_type(self, purpose: int, hints: int) -> None: ...
    def do_set_cursor_location(self, x: int, y: int, w: int, h: int) -> None: ...
    def do_set_surrounding_text(
        self, text: Text, cursor_index: int, anchor_pos: int
    ) -> None: ...
    def forward_key_event(self, keyval: int, keycode: int, state: int) -> None: ...
    def get_content_type(self) -> typing.Tuple[int, int]: ...
    def get_name(self) -> str: ...
    def get_surrounding_text(self) -> typing.Tuple[Text, int, int]: ...
    def hide_auxiliary_text(self) -> None: ...
    def hide_lookup_table(self) -> None: ...
    def hide_preedit_text(self) -> None: ...
    @classmethod
    def new(
        cls, engine_name: str, object_path: str, connection: Gio.DBusConnection
    ) -> Engine: ...
    @classmethod
    def new_with_type(
        cls,
        engine_type: typing.Type[typing.Any],
        engine_name: str,
        object_path: str,
        connection: Gio.DBusConnection,
    ) -> Engine: ...
    def register_properties(self, prop_list: PropList) -> None: ...
    def show_auxiliary_text(self) -> None: ...
    def show_lookup_table(self) -> None: ...
    def show_preedit_text(self) -> None: ...
    def update_auxiliary_text(self, text: Text, visible: bool) -> None: ...
    def update_lookup_table(self, lookup_table: LookupTable, visible: bool) -> None: ...
    def update_lookup_table_fast(
        self, lookup_table: LookupTable, visible: bool
    ) -> None: ...
    def update_preedit_text(
        self, text: Text, cursor_pos: int, visible: bool
    ) -> None: ...
    def update_preedit_text_with_mode(
        self, text: Text, cursor_pos: int, visible: bool, mode: PreeditFocusMode
    ) -> None: ...
    def update_property(self, prop: Property) -> None: ...

class EngineClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EngineClass()
    """

    parent: ServiceClass = ...
    process_key_event: typing.Callable[[Engine, int, int, int], bool] = ...
    focus_in: typing.Callable[[Engine], None] = ...
    focus_out: typing.Callable[[Engine], None] = ...
    reset: typing.Callable[[Engine], None] = ...
    enable: typing.Callable[[Engine], None] = ...
    disable: typing.Callable[[Engine], None] = ...
    set_cursor_location: typing.Callable[[Engine, int, int, int, int], None] = ...
    set_capabilities: typing.Callable[[Engine, int], None] = ...
    page_up: typing.Callable[[Engine], None] = ...
    page_down: typing.Callable[[Engine], None] = ...
    cursor_up: typing.Callable[[Engine], None] = ...
    cursor_down: typing.Callable[[Engine], None] = ...
    property_activate: typing.Callable[[Engine, str, int], None] = ...
    property_show: typing.Callable[[Engine, str], None] = ...
    property_hide: typing.Callable[[Engine, str], None] = ...
    candidate_clicked: typing.Callable[[Engine, int, int, int], None] = ...
    set_surrounding_text: typing.Callable[[Engine, Text, int, int], None] = ...
    process_hand_writing_event: typing.Callable[[Engine, float, int], None] = ...
    cancel_hand_writing: typing.Callable[[Engine, int], None] = ...
    set_content_type: typing.Callable[[Engine, int, int], None] = ...
    focus_in_id: typing.Callable[[Engine, str, str], None] = ...
    focus_out_id: typing.Callable[[Engine, str], None] = ...
    pdummy: list[None] = ...

class EngineDesc(Serializable):
    """
    :Constructors:

    ::

        EngineDesc(**properties)
        new(name:str, longname:str, description:str, language:str, license:str, author:str, icon:str, layout:str) -> IBus.EngineDesc
        new_from_xml_node(node:IBus.XML) -> IBus.EngineDesc

    Object IBusEngineDesc

    Properties from IBusEngineDesc:
      name -> gchararray: description name
        The name of engine description
      longname -> gchararray: description longname
        The longname of engine description
      description -> gchararray: description description
        The description of engine description
      language -> gchararray: description language
        The language of engine description
      license -> gchararray: description license
        The license of engine description
      author -> gchararray: description author
        The author of engine description
      icon -> gchararray: description icon
        The icon of engine description
      layout -> gchararray: description layout
        The layout of engine description
      layout-variant -> gchararray: description keyboard variant
        The keyboard variant of engine description
      layout-option -> gchararray: description keyboard option
        The keyboard option of engine description
      rank -> guint: description rank
        The rank of engine description
      hotkeys -> gchararray: description hotkeys
        The hotkeys of engine description
      symbol -> gchararray: description symbol
        The icon symbol chars of engine description
      setup -> gchararray: setup args
        The exec lists of the engine setup command
      version -> gchararray: version number
        The version number of engine description
      textdomain -> gchararray: textdomain
        The textdomain of engine description
      icon-prop-key -> gchararray: icon property key
        The key of IBusProperty for the dynamic panel icon

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        author: str
        description: str
        hotkeys: str
        icon: str
        icon_prop_key: str
        language: str
        layout: str
        layout_option: str
        layout_variant: str
        license: str
        longname: str
        name: str
        rank: int
        setup: str
        symbol: str
        textdomain: str
        version: str

    props: Props = ...
    parent: Serializable = ...
    priv: EngineDescPrivate = ...
    def __init__(
        self,
        author: str = ...,
        description: str = ...,
        hotkeys: str = ...,
        icon: str = ...,
        icon_prop_key: str = ...,
        language: str = ...,
        layout: str = ...,
        layout_option: str = ...,
        layout_variant: str = ...,
        license: str = ...,
        longname: str = ...,
        name: str = ...,
        rank: int = ...,
        setup: str = ...,
        symbol: str = ...,
        textdomain: str = ...,
        version: str = ...,
    ) -> None: ...
    def get_author(self) -> str: ...
    def get_description(self) -> str: ...
    def get_hotkeys(self) -> str: ...
    def get_icon(self) -> str: ...
    def get_icon_prop_key(self) -> str: ...
    def get_language(self) -> str: ...
    def get_layout(self) -> str: ...
    def get_layout_option(self) -> str: ...
    def get_layout_variant(self) -> str: ...
    def get_license(self) -> str: ...
    def get_longname(self) -> str: ...
    def get_name(self) -> str: ...
    def get_rank(self) -> int: ...
    def get_setup(self) -> str: ...
    def get_symbol(self) -> str: ...
    def get_textdomain(self) -> str: ...
    def get_version(self) -> str: ...
    @classmethod
    def new(
        cls,
        name: str,
        longname: str,
        description: str,
        language: str,
        license: str,
        author: str,
        icon: str,
        layout: str,
    ) -> EngineDesc: ...
    @classmethod
    def new_from_xml_node(cls, node: XML) -> EngineDesc: ...
    def output(self, output: GLib.String, indent: int) -> None: ...

class EngineDescClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EngineDescClass()
    """

    parent: SerializableClass = ...

class EngineDescPrivate(GObject.GPointer): ...
class EnginePrivate(GObject.GPointer): ...

class EngineSimple(Engine):
    """
    :Constructors:

    ::

        EngineSimple(**properties)

    Object IBusEngineSimple

    Signals from IBusEngine:
      process-key-event (guint, guint, guint) -> gboolean
      focus-in ()
      focus-in-id (gchararray, gchararray)
      focus-out ()
      focus-out-id (gchararray)
      reset ()
      enable ()
      disable ()
      set-cursor-location (gint, gint, gint, gint)
      set-capabilities (guint)
      page-up ()
      page-down ()
      cursor-up ()
      cursor-down ()
      candidate-clicked (guint, guint, guint)
      property-activate (gchararray, guint)
      property-show (gchararray)
      property-hide (gchararray)
      process-hand-writing-event (gpointer, guint)
      cancel-hand-writing (guint)
      set-surrounding-text (GObject, guint, guint)
      set-content-type (guint, guint)

    Properties from IBusEngine:
      engine-name -> gchararray: engine name
        engine name
      has-focus-id -> gboolean: has focus id
        Has focus ID
      active-surrounding-text -> gboolean: enable surrounding text update by focus event
        Enable surrounding text update by focus event

    Properties from IBusService:
      object-path -> gchararray: object path
        The path of service object
      connection -> GDBusConnection: connection
        The connection of service object

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        active_surrounding_text: bool
        engine_name: str
        has_focus_id: bool
        connection: Gio.DBusConnection
        object_path: str

    props: Props = ...
    parent: Engine = ...
    priv: EngineSimplePrivate = ...
    def __init__(
        self,
        active_surrounding_text: bool = ...,
        engine_name: str = ...,
        has_focus_id: bool = ...,
        connection: Gio.DBusConnection = ...,
        object_path: str = ...,
    ) -> None: ...
    def add_compose_file(self, file: str) -> bool: ...
    def add_table(
        self, data: typing.Sequence[int], max_seq_len: int, n_seqs: int
    ) -> None: ...
    def add_table_by_locale(self, locale: typing.Optional[str] = None) -> bool: ...

class EngineSimpleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EngineSimpleClass()
    """

    parent: EngineClass = ...
    pdummy: list[None] = ...

class EngineSimplePrivate(GObject.GPointer): ...

class ExtensionEvent(Serializable):
    """
    :Constructors:

    ::

        ExtensionEvent(**properties)

    Object IBusExtensionEvent

    Properties from IBusExtensionEvent:
      version -> guint: version
        version
      name -> gchararray: name
        name of the extension
      is-enabled -> gboolean: is enabled
        if the extension is enabled
      is-extension -> gboolean: is extension
        if the event is called by an extension
      params -> gchararray: params
        Parameters to enable the extension

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        is_enabled: bool
        is_extension: bool
        name: str
        params: str
        version: int

    props: Props = ...
    parent: Serializable = ...
    priv: ExtensionEventPrivate = ...
    def __init__(
        self,
        is_enabled: bool = ...,
        is_extension: bool = ...,
        name: str = ...,
        params: str = ...,
    ) -> None: ...
    def get_name(self) -> str: ...
    def get_params(self) -> str: ...
    def get_version(self) -> int: ...
    def is_enabled(self) -> bool: ...
    def is_extension(self) -> bool: ...

class ExtensionEventClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ExtensionEventClass()
    """

    parent: SerializableClass = ...
    pdummy: list[None] = ...

class ExtensionEventPrivate(GObject.GPointer): ...

class Factory(Service):
    """
    :Constructors:

    ::

        Factory(**properties)
        new(connection:Gio.DBusConnection) -> IBus.Factory

    Object IBusFactory

    Signals from IBusFactory:
      create-engine (gchararray) -> IBusEngine

    Properties from IBusService:
      object-path -> gchararray: object path
        The path of service object
      connection -> GDBusConnection: connection
        The connection of service object

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        connection: Gio.DBusConnection
        object_path: str

    props: Props = ...
    parent: Service = ...
    priv: FactoryPrivate = ...
    def __init__(
        self, connection: Gio.DBusConnection = ..., object_path: str = ...
    ) -> None: ...
    def add_engine(
        self, engine_name: str, engine_type: typing.Type[typing.Any]
    ) -> None: ...
    def create_engine(self, engine_name: str) -> Engine: ...
    def do_create_engine(self, engine_name: str) -> Engine: ...
    @classmethod
    def new(cls, connection: Gio.DBusConnection) -> Factory: ...

class FactoryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FactoryClass()
    """

    parent: ServiceClass = ...
    create_engine: typing.Callable[[Factory, str], Engine] = ...
    pdummy: list[None] = ...

class FactoryPrivate(GObject.GPointer): ...

class HotkeyProfile(Serializable):
    """
    :Constructors:

    ::

        HotkeyProfile(**properties)
        new() -> IBus.HotkeyProfile

    Object IBusHotkeyProfile

    Signals from IBusHotkeyProfile:
      trigger (guint, gpointer)

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable = ...
    def add_hotkey(self, keyval: int, modifiers: int, event: int) -> bool: ...
    def add_hotkey_from_string(self, str: str, event: int) -> bool: ...
    def do_trigger(self, event: int, *user_data: typing.Any) -> None: ...
    def filter_key_event(
        self,
        keyval: int,
        modifiers: int,
        prev_keyval: int,
        prev_modifiers: int,
        user_data: None,
    ) -> int: ...
    def lookup_hotkey(self, keyval: int, modifiers: int) -> int: ...
    @classmethod
    def new(cls) -> HotkeyProfile: ...
    def remove_hotkey(self, keyval: int, modifiers: int) -> bool: ...
    def remove_hotkey_by_event(self, event: int) -> bool: ...

class HotkeyProfileClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HotkeyProfileClass()
    """

    parent: SerializableClass = ...
    trigger: typing.Callable[..., None] = ...

class InputContext(Proxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable):
    """
    :Constructors:

    ::

        InputContext(**properties)
        new(path:str, connection:Gio.DBusConnection, cancellable:Gio.Cancellable=None) -> IBus.InputContext
        new_async_finish(res:Gio.AsyncResult) -> IBus.InputContext

    Object IBusInputContext

    Signals from IBusInputContext:
      enabled ()
      disabled ()
      commit-text (IBusText)
      forward-key-event (guint, guint, guint)
      delete-surrounding-text (gint, guint)
      update-preedit-text (IBusText, guint, gboolean)
      update-preedit-text-with-mode (IBusText, guint, gboolean, guint)
      show-preedit-text ()
      hide-preedit-text ()
      update-auxiliary-text (IBusText, gboolean)
      show-auxiliary-text ()
      hide-auxiliary-text ()
      update-lookup-table (IBusLookupTable, gboolean)
      show-lookup-table ()
      hide-lookup-table ()
      page-up-lookup-table ()
      page-down-lookup-table ()
      cursor-up-lookup-table ()
      cursor-down-lookup-table ()
      register-properties (IBusPropList)
      update-property (IBusProperty)
      require-surrounding-text ()

    Signals from IBusProxy:
      destroy ()

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
      g-bus-type -> GBusType: g-bus-type
      g-name -> gchararray: g-name
      g-name-owner -> gchararray: g-name-owner
      g-flags -> GDBusProxyFlags: g-flags
      g-object-path -> gchararray: g-object-path
      g-interface-name -> gchararray: g-interface-name
      g-default-timeout -> gint: g-default-timeout
      g-interface-info -> GDBusInterfaceInfo: g-interface-info

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    props: Props = ...
    parent: Proxy = ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ) -> None: ...
    def cancel_hand_writing(self, n_strokes: int) -> None: ...
    def focus_in(self) -> None: ...
    def focus_out(self) -> None: ...
    def get_engine(self) -> EngineDesc: ...
    def get_engine_async(
        self,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def get_engine_async_finish(self, res: Gio.AsyncResult) -> EngineDesc: ...
    @staticmethod
    def get_input_context(
        path: str, connection: Gio.DBusConnection
    ) -> InputContext: ...
    @staticmethod
    def get_input_context_async(
        path: str,
        connection: Gio.DBusConnection,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @staticmethod
    def get_input_context_async_finish(res: Gio.AsyncResult) -> InputContext: ...
    def needs_surrounding_text(self) -> bool: ...
    @classmethod
    def new(
        cls,
        path: str,
        connection: Gio.DBusConnection,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> InputContext: ...
    @staticmethod
    def new_async(
        path: str,
        connection: Gio.DBusConnection,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @classmethod
    def new_async_finish(cls, res: Gio.AsyncResult) -> InputContext: ...
    def post_process_key_event(self) -> None: ...
    def process_hand_writing_event(
        self, coordinates: float, coordinates_len: int
    ) -> None: ...
    def process_key_event(self, keyval: int, keycode: int, state: int) -> bool: ...
    def process_key_event_async(
        self,
        keyval: int,
        keycode: int,
        state: int,
        timeout_msec: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def process_key_event_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def property_activate(self, prop_name: str, state: int) -> None: ...
    def reset(self) -> None: ...
    def set_capabilities(self, capabilities: int) -> None: ...
    def set_client_commit_preedit(self, client_commit: bool) -> None: ...
    def set_content_type(self, purpose: int, hints: int) -> None: ...
    def set_cursor_location(self, x: int, y: int, w: int, h: int) -> None: ...
    def set_cursor_location_relative(self, x: int, y: int, w: int, h: int) -> None: ...
    def set_engine(self, name: str) -> None: ...
    def set_post_process_key_event(self, enable: bool) -> None: ...
    def set_surrounding_text(
        self, text: Text, cursor_pos: int, anchor_pos: int
    ) -> None: ...

class InputContextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InputContextClass()
    """

    parent: ProxyClass = ...
    pdummy: list[None] = ...

class Keymap(Object):
    """
    :Constructors:

    ::

        Keymap(**properties)
        new(name:str) -> IBus.Keymap

    Object IBusKeymap

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Object = ...
    name: str = ...
    keymap: list[int] = ...
    @staticmethod
    def get(name: str) -> Keymap: ...
    def lookup_keysym(self, keycode: int, state: int) -> int: ...
    @classmethod
    def new(cls, name: str) -> Keymap: ...

class KeymapClass(GObject.GPointer):
    """
    :Constructors:

    ::

        KeymapClass()
    """

    parent: ObjectClass = ...

class LookupTable(Serializable):
    """
    :Constructors:

    ::

        LookupTable(**properties)
        new(page_size:int, cursor_pos:int, cursor_visible:bool, round:bool) -> IBus.LookupTable

    Object IBusLookupTable

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable = ...
    page_size: int = ...
    cursor_pos: int = ...
    cursor_visible: bool = ...
    round: bool = ...
    orientation: int = ...
    candidates: list[None] = ...
    labels: list[None] = ...
    def append_candidate(self, text: Text) -> None: ...
    def append_label(self, text: Text) -> None: ...
    def clean(self): ...  # FIXME Function
    def clear(self) -> None: ...
    def cursor_down(self) -> bool: ...
    def cursor_up(self) -> bool: ...
    def get_candidate(self, index: int) -> Text: ...
    def get_cursor_in_page(self) -> int: ...
    def get_cursor_pos(self) -> int: ...
    def get_label(self, index: int) -> Text: ...
    def get_number_of_candidates(self) -> int: ...
    def get_orientation(self) -> int: ...
    def get_page_size(self) -> int: ...
    def is_cursor_visible(self) -> bool: ...
    def is_round(self) -> bool: ...
    @classmethod
    def new(
        cls, page_size: int, cursor_pos: int, cursor_visible: bool, round: bool
    ) -> LookupTable: ...
    def page_down(self) -> bool: ...
    def page_up(self) -> bool: ...
    def set_cursor_pos(self, cursor_pos: int) -> None: ...
    def set_cursor_visible(self, visible: bool) -> None: ...
    def set_label(self, index: int, text: Text) -> None: ...
    def set_orientation(self, orientation: int) -> None: ...
    def set_page_size(self, page_size: int) -> None: ...
    def set_round(self, round: bool) -> None: ...
    def show_cursor(self, visible): ...  # FIXME Function

class LookupTableClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LookupTableClass()
    """

    parent: SerializableClass = ...

class Object(GObject.InitiallyUnowned):
    """
    :Constructors:

    ::

        Object(**properties)
        new() -> IBus.Object

    Object IBusObject

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.InitiallyUnowned = ...
    flags: int = ...
    priv: ObjectPrivate = ...
    def destroy(self) -> None: ...
    def do_destroy(self) -> None: ...
    @classmethod
    def new(cls) -> Object: ...

class ObjectClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectClass()
    """

    parent: GObject.InitiallyUnownedClass = ...
    destroy: typing.Callable[[Object], None] = ...
    pdummy: list[None] = ...

class ObjectPrivate(GObject.GPointer): ...

class ObservedPath(Serializable):
    """
    :Constructors:

    ::

        ObservedPath(**properties)
        new(path:str, fill_stat:bool) -> IBus.ObservedPath
        new_from_xml_node(node:IBus.XML, fill_stat:bool) -> IBus.ObservedPath

    Object IBusObservedPath

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable = ...
    path: str = ...
    mtime: int = ...
    is_dir: bool = ...
    is_exist: bool = ...
    def check_modification(self) -> bool: ...
    @classmethod
    def new(cls, path: str, fill_stat: bool) -> ObservedPath: ...
    @classmethod
    def new_from_xml_node(cls, node: XML, fill_stat: bool) -> ObservedPath: ...
    def output(self, output: GLib.String, indent: int) -> None: ...
    def traverse(self, dir_only: bool) -> list[ObservedPath]: ...

class ObservedPathClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObservedPathClass()
    """

    parent: SerializableClass = ...

class PanelService(Service):
    """
    :Constructors:

    ::

        PanelService(**properties)
        new(connection:Gio.DBusConnection) -> IBus.PanelService

    Object IBusPanelService

    Signals from IBusPanelService:
      process-key-event (guint, guint, guint) -> gboolean
      focus-in (gchararray)
      focus-out (gchararray)
      reset ()
      set-cursor-location (gint, gint, gint, gint)
      set-content-type (guint, guint)
      update-preedit-text (IBusText, guint, gboolean)
      show-preedit-text ()
      hide-preedit-text ()
      update-auxiliary-text (IBusText, gboolean)
      show-auxiliary-text ()
      hide-auxiliary-text ()
      update-lookup-table (IBusLookupTable, gboolean)
      show-lookup-table ()
      hide-lookup-table ()
      page-up-lookup-table ()
      page-down-lookup-table ()
      cursor-up-lookup-table ()
      cursor-down-lookup-table ()
      register-properties (IBusPropList)
      update-property (IBusProperty)
      set-cursor-location-relative (gint, gint, gint, gint)
      hide-language-bar ()
      show-language-bar ()
      start-setup ()
      state-changed ()
      destroy-context (gchararray)
      panel-extension-received (IBusExtensionEvent)
      commit-text-received (IBusText)
      candidate-clicked-lookup-table (guint, guint, guint)

    Properties from IBusService:
      object-path -> gchararray: object path
        The path of service object
      connection -> GDBusConnection: connection
        The connection of service object

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        connection: Gio.DBusConnection
        object_path: str

    props: Props = ...
    parent: Service = ...
    def __init__(
        self, connection: Gio.DBusConnection = ..., object_path: str = ...
    ) -> None: ...
    def candidate_clicked(self, index: int, button: int, state: int) -> None: ...
    def commit_text(self, text: Text) -> None: ...
    def cursor_down(self) -> None: ...
    def cursor_up(self) -> None: ...
    def do_candidate_clicked_lookup_table(
        self, index: int, button: int, state: int
    ) -> None: ...
    def do_commit_text_received(self, text: Text) -> None: ...
    def do_cursor_down_lookup_table(self) -> None: ...
    def do_cursor_up_lookup_table(self) -> None: ...
    def do_destroy_context(self, input_context_path: str) -> None: ...
    def do_focus_in(self, input_context_path: str) -> None: ...
    def do_focus_out(self, input_context_path: str) -> None: ...
    def do_hide_auxiliary_text(self) -> None: ...
    def do_hide_language_bar(self) -> None: ...
    def do_hide_lookup_table(self) -> None: ...
    def do_hide_preedit_text(self) -> None: ...
    def do_page_down_lookup_table(self) -> None: ...
    def do_page_up_lookup_table(self) -> None: ...
    def do_panel_extension_received(self, event: ExtensionEvent) -> None: ...
    def do_process_key_event(self, keyval: int, keycode: int, state: int) -> bool: ...
    def do_register_properties(self, prop_list: PropList) -> None: ...
    def do_reset(self) -> None: ...
    def do_set_content_type(self, purpose: int, hints: int) -> None: ...
    def do_set_cursor_location(self, x: int, y: int, w: int, h: int) -> None: ...
    def do_set_cursor_location_relative(
        self, x: int, y: int, w: int, h: int
    ) -> None: ...
    def do_show_auxiliary_text(self) -> None: ...
    def do_show_language_bar(self) -> None: ...
    def do_show_lookup_table(self) -> None: ...
    def do_show_preedit_text(self) -> None: ...
    def do_start_setup(self) -> None: ...
    def do_state_changed(self) -> None: ...
    def do_update_auxiliary_text(self, text: Text, visible: bool) -> None: ...
    def do_update_lookup_table(
        self, lookup_table: LookupTable, visible: bool
    ) -> None: ...
    def do_update_preedit_text(
        self, text: Text, cursor_pos: int, visible: bool
    ) -> None: ...
    def do_update_property(self, prop: Property) -> None: ...
    def hide_preedit_text_received(self) -> None: ...
    @classmethod
    def new(cls, connection: Gio.DBusConnection) -> PanelService: ...
    def page_down(self) -> None: ...
    def page_up(self) -> None: ...
    def panel_extension(self, event: ExtensionEvent) -> None: ...
    def property_activate(self, prop_name: str, prop_state: int) -> None: ...
    def property_hide(self, prop_name: str) -> None: ...
    def property_show(self, prop_name: str) -> None: ...
    def show_preedit_text_received(self) -> None: ...
    def update_auxiliary_text_received(self, text: Text, visible: bool) -> None: ...
    def update_lookup_table_received(
        self, table: LookupTable, visible: bool
    ) -> None: ...
    def update_preedit_text_received(
        self, text: Text, cursor_pos: int, visible: bool
    ) -> None: ...

class PanelServiceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PanelServiceClass()
    """

    parent: ServiceClass = ...
    focus_in: typing.Callable[[PanelService, str], None] = ...
    focus_out: typing.Callable[[PanelService, str], None] = ...
    register_properties: typing.Callable[[PanelService, PropList], None] = ...
    set_cursor_location: typing.Callable[[PanelService, int, int, int, int], None] = ...
    update_auxiliary_text: typing.Callable[[PanelService, Text, bool], None] = ...
    update_lookup_table: typing.Callable[[PanelService, LookupTable, bool], None] = ...
    update_preedit_text: typing.Callable[[PanelService, Text, int, bool], None] = ...
    update_property: typing.Callable[[PanelService, Property], None] = ...
    cursor_down_lookup_table: typing.Callable[[PanelService], None] = ...
    cursor_up_lookup_table: typing.Callable[[PanelService], None] = ...
    hide_auxiliary_text: typing.Callable[[PanelService], None] = ...
    hide_language_bar: typing.Callable[[PanelService], None] = ...
    hide_lookup_table: typing.Callable[[PanelService], None] = ...
    hide_preedit_text: typing.Callable[[PanelService], None] = ...
    page_down_lookup_table: typing.Callable[[PanelService], None] = ...
    page_up_lookup_table: typing.Callable[[PanelService], None] = ...
    reset: typing.Callable[[PanelService], None] = ...
    show_auxiliary_text: typing.Callable[[PanelService], None] = ...
    show_language_bar: typing.Callable[[PanelService], None] = ...
    show_lookup_table: typing.Callable[[PanelService], None] = ...
    show_preedit_text: typing.Callable[[PanelService], None] = ...
    start_setup: typing.Callable[[PanelService], None] = ...
    state_changed: typing.Callable[[PanelService], None] = ...
    destroy_context: typing.Callable[[PanelService, str], None] = ...
    set_content_type: typing.Callable[[PanelService, int, int], None] = ...
    set_cursor_location_relative: typing.Callable[
        [PanelService, int, int, int, int], None
    ] = ...
    panel_extension_received: typing.Callable[[PanelService, ExtensionEvent], None] = (
        ...
    )
    process_key_event: typing.Callable[[PanelService, int, int, int], bool] = ...
    commit_text_received: typing.Callable[[PanelService, Text], None] = ...
    candidate_clicked_lookup_table: typing.Callable[
        [PanelService, int, int, int], None
    ] = ...
    pdummy: list[None] = ...

class ProcessKeyEventData(GObject.GPointer):
    """
    :Constructors:

    ::

        ProcessKeyEventData()
    """

    keyval: int = ...
    keycode: int = ...
    state: int = ...

class PropList(Serializable):
    """
    :Constructors:

    ::

        PropList(**properties)
        new() -> IBus.PropList

    Object IBusPropList

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable = ...
    properties: list[None] = ...
    def append(self, prop: Property) -> None: ...
    def get(self, index: int) -> Property: ...
    @classmethod
    def new(cls) -> PropList: ...
    def update_property(self, prop: Property) -> bool: ...

class PropListClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PropListClass()
    """

    parent: SerializableClass = ...

class Property(Serializable):
    """
    :Constructors:

    ::

        Property(**properties)
        new(key:str, type:IBus.PropType, label:IBus.Text, icon:str=None, tooltip:IBus.Text, sensitive:bool, visible:bool, state:IBus.PropState, prop_list:IBus.PropList=None) -> IBus.Property

    Object IBusProperty

    Properties from IBusProperty:
      key -> gchararray: key
        The key of property
      icon -> gchararray: icon
        The icon of property
      label -> IBusText: label
        The label of property
      symbol -> IBusText: symbol
        The symbol of property
      tooltip -> IBusText: tooltip
        The tooltip of property
      sensitive -> gboolean: sensitive
        The sensitive of property
      visible -> gboolean: visible
        The visible of property
      prop-type -> IBusPropType: prop-type
        The type of property
      state -> IBusPropState: state
        The state of property
      sub-props -> IBusPropList: sub properties
        The sub properties of property

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        icon: str
        key: str
        label: Text
        prop_type: PropType
        sensitive: bool
        state: PropState
        sub_props: PropList
        symbol: Text
        tooltip: Text
        visible: bool

    props: Props = ...
    parent: Serializable = ...
    priv: PropertyPrivate = ...
    pdummy: list[None] = ...
    def __init__(
        self,
        icon: str = ...,
        key: str = ...,
        label: Text = ...,
        prop_type: PropType = ...,
        sensitive: bool = ...,
        state: PropState = ...,
        sub_props: PropList = ...,
        symbol: Text = ...,
        tooltip: Text = ...,
        visible: bool = ...,
    ) -> None: ...
    def get_icon(self) -> str: ...
    def get_key(self) -> str: ...
    def get_label(self) -> Text: ...
    def get_prop_type(self) -> PropType: ...
    def get_sensitive(self) -> bool: ...
    def get_state(self) -> PropState: ...
    def get_sub_props(self) -> PropList: ...
    def get_symbol(self) -> Text: ...
    def get_tooltip(self) -> Text: ...
    def get_visible(self) -> bool: ...
    @classmethod
    def new(
        cls,
        key: str,
        type: PropType,
        label: Text,
        icon: typing.Optional[str],
        tooltip: Text,
        sensitive: bool,
        visible: bool,
        state: PropState,
        prop_list: typing.Optional[PropList] = None,
    ) -> Property: ...
    def set_icon(self, icon: str) -> None: ...
    def set_label(self, label: Text) -> None: ...
    def set_sensitive(self, sensitive: bool) -> None: ...
    def set_state(self, state: PropState) -> None: ...
    def set_sub_props(self, prop_list: PropList) -> None: ...
    def set_symbol(self, symbol: Text) -> None: ...
    def set_tooltip(self, tooltip: Text) -> None: ...
    def set_visible(self, visible: bool) -> None: ...
    def update(self, prop_update: Property) -> bool: ...

class PropertyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PropertyClass()
    """

    parent: SerializableClass = ...

class PropertyPrivate(GObject.GPointer): ...

class Proxy(Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable):
    """
    :Constructors:

    ::

        Proxy(**properties)

    Object IBusProxy

    Signals from IBusProxy:
      destroy ()

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
      g-bus-type -> GBusType: g-bus-type
      g-name -> gchararray: g-name
      g-name-owner -> gchararray: g-name-owner
      g-flags -> GDBusProxyFlags: g-flags
      g-object-path -> gchararray: g-object-path
      g-interface-name -> gchararray: g-interface-name
      g-default-timeout -> gint: g-default-timeout
      g-interface-info -> GDBusInterfaceInfo: g-interface-info

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    props: Props = ...
    parent: Gio.DBusProxy = ...
    flags: int = ...
    own: bool = ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ) -> None: ...
    def destroy(self) -> None: ...
    def do_destroy(self) -> None: ...

class ProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ProxyClass()
    """

    parent: Gio.DBusProxyClass = ...
    destroy: typing.Callable[[Proxy], None] = ...
    pdummy: list[None] = ...

class Rectangle(GObject.GPointer):
    """
    :Constructors:

    ::

        Rectangle()
    """

    x: int = ...
    y: int = ...
    width: int = ...
    height: int = ...

class Registry(Serializable):
    """
    :Constructors:

    ::

        Registry(**properties)
        new() -> IBus.Registry

    Object IBusRegistry

    Signals from IBusRegistry:
      changed ()

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable = ...
    priv: RegistryPrivate = ...
    def check_modification(self) -> bool: ...
    def get_components(self) -> list[Component]: ...
    def get_observed_paths(self) -> list[ObservedPath]: ...
    def load(self) -> None: ...
    def load_cache(self, is_user: bool) -> bool: ...
    def load_cache_file(self, filename: str) -> bool: ...
    def load_in_dir(self, dirname: str) -> None: ...
    @classmethod
    def new(cls) -> Registry: ...
    def output(self, output: GLib.String, indent: int) -> None: ...
    def save_cache(self, is_user: bool) -> bool: ...
    def save_cache_file(self, filename: str) -> bool: ...
    def start_monitor_changes(self) -> None: ...

class RegistryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RegistryClass()
    """

    parent: SerializableClass = ...

class RegistryPrivate(GObject.GPointer): ...

class Serializable(Object):
    """
    :Constructors:

    ::

        Serializable(**properties)
        new() -> IBus.Serializable

    Object IBusSerializable

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Object = ...
    priv: SerializablePrivate = ...
    def copy(self) -> Serializable: ...
    @staticmethod
    def deserialize_object(variant: GLib.Variant) -> Serializable: ...
    def do_copy(self, src: Serializable) -> bool: ...
    def do_deserialize(self, variant: GLib.Variant) -> int: ...
    def do_serialize(self, builder: GLib.VariantBuilder) -> bool: ...
    def get_qattachment(self, key: int) -> GLib.Variant: ...
    @classmethod
    def new(cls) -> Serializable: ...
    def remove_qattachment(self, key: int) -> None: ...
    def serialize_object(self) -> GLib.Variant: ...
    def set_qattachment(self, key: int, value: GLib.Variant) -> None: ...

class SerializableClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SerializableClass()
    """

    parent: ObjectClass = ...
    serialize: typing.Callable[[Serializable, GLib.VariantBuilder], bool] = ...
    deserialize: typing.Callable[[Serializable, GLib.Variant], int] = ...
    copy: typing.Callable[[Serializable, Serializable], bool] = ...
    pdummy: list[None] = ...

class SerializablePrivate(GObject.GPointer): ...

class Service(Object):
    """
    :Constructors:

    ::

        Service(**properties)
        new(connection:Gio.DBusConnection, path:str) -> IBus.Service

    Object IBusService

    Properties from IBusService:
      object-path -> gchararray: object path
        The path of service object
      connection -> GDBusConnection: connection
        The connection of service object

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        connection: Gio.DBusConnection
        object_path: str

    props: Props = ...
    parent: Object = ...
    priv: ServicePrivate = ...
    def __init__(
        self, connection: Gio.DBusConnection = ..., object_path: str = ...
    ) -> None: ...
    def add_interfaces(self, xml_data: str) -> bool: ...
    def do_service_get_property(
        self,
        connection: Gio.DBusConnection,
        sender: str,
        object_path: str,
        interface_name: str,
        property_name: str,
    ) -> typing.Optional[GLib.Variant]: ...
    def do_service_method_call(
        self,
        connection: Gio.DBusConnection,
        sender: str,
        object_path: str,
        interface_name: str,
        method_name: str,
        parameters: GLib.Variant,
        invocation: Gio.DBusMethodInvocation,
    ) -> None: ...
    def do_service_set_property(
        self,
        connection: Gio.DBusConnection,
        sender: str,
        object_path: str,
        interface_name: str,
        property_name: str,
        value: GLib.Variant,
    ) -> bool: ...
    def emit_signal(
        self,
        dest_bus_name: str,
        interface_name: str,
        signal_name: str,
        parameters: GLib.Variant,
    ) -> bool: ...
    def free_interfaces(self, depth: int) -> int: ...
    def get_connection(self) -> Gio.DBusConnection: ...
    def get_object_path(self) -> str: ...
    @classmethod
    def new(cls, connection: Gio.DBusConnection, path: str) -> Service: ...
    def register(self, connection: Gio.DBusConnection) -> bool: ...
    def unregister(self, connection: Gio.DBusConnection) -> None: ...

class ServiceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ServiceClass()
    """

    parent: ObjectClass = ...
    service_method_call: typing.Callable[
        [
            Service,
            Gio.DBusConnection,
            str,
            str,
            str,
            str,
            GLib.Variant,
            Gio.DBusMethodInvocation,
        ],
        None,
    ] = ...
    service_get_property: typing.Callable[
        [Service, Gio.DBusConnection, str, str, str, str], typing.Optional[GLib.Variant]
    ] = ...
    service_set_property: typing.Callable[
        [Service, Gio.DBusConnection, str, str, str, str, GLib.Variant], bool
    ] = ...
    interfaces: list[None] = ...
    pdummy: list[None] = ...
    def add_interfaces(self, xml_data: str) -> bool: ...
    def free_interfaces(self, depth: int) -> int: ...

class ServicePrivate(GObject.GPointer): ...

class Text(Serializable):
    """
    :Constructors:

    ::

        Text(**properties)
        new_from_string(str:str) -> IBus.Text
        new_from_ucs4(str:str) -> IBus.Text
        new_from_unichar(c:str) -> IBus.Text

    Object IBusText

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable = ...
    is_static: bool = ...
    text: str = ...
    attrs: AttrList = ...
    def append_attribute(
        self, type: int, value: int, start_index: int, end_index: int
    ) -> None: ...
    def get_attributes(self) -> AttrList: ...
    def get_length(self) -> int: ...
    def get_text(self) -> str: ...
    @classmethod
    def new_from_string(cls, str: str) -> Text: ...
    @classmethod
    def new_from_ucs4(cls, str: str) -> Text: ...
    @classmethod
    def new_from_unichar(cls, c: str) -> Text: ...
    def set_attributes(self, attrs: AttrList) -> None: ...

class TextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TextClass()
    """

    parent: SerializableClass = ...

class UnicodeBlock(Serializable):
    """
    :Constructors:

    ::

        UnicodeBlock(**properties)

    Object IBusUnicodeBlock

    Properties from IBusUnicodeBlock:
      name -> gchararray: name
        The Unicode name
      start -> guint: start code point
        The Unicode start code point
      end -> guint: end code point
        The Unicode end code point

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        end: int
        name: str
        start: int

    props: Props = ...
    parent: Serializable = ...
    priv: UnicodeBlockPrivate = ...
    def __init__(self, end: int = ..., name: str = ..., start: int = ...) -> None: ...
    def get_end(self) -> str: ...
    def get_name(self) -> str: ...
    def get_start(self) -> str: ...
    @staticmethod
    def load(path: str) -> list[UnicodeBlock]: ...
    @staticmethod
    def save(path: str, list: list[UnicodeBlock]) -> None: ...

class UnicodeBlockClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UnicodeBlockClass()
    """

    parent: SerializableClass = ...

class UnicodeBlockPrivate(GObject.GPointer): ...

class UnicodeData(Serializable):
    """
    :Constructors:

    ::

        UnicodeData(**properties)

    Object IBusUnicodeData

    Properties from IBusUnicodeData:
      code -> guint: code point
        The Unicode code point
      name -> gchararray: name
        The Unicode name
      alias -> gchararray: alias name
        The Unicode alias name
      block-name -> gchararray: block name
        The Unicode block name

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        alias: str
        block_name: str
        code: int
        name: str

    props: Props = ...
    parent: Serializable = ...
    priv: UnicodeDataPrivate = ...
    def __init__(
        self, alias: str = ..., block_name: str = ..., code: int = ..., name: str = ...
    ) -> None: ...
    def get_alias(self) -> str: ...
    def get_block_name(self) -> str: ...
    def get_code(self) -> str: ...
    def get_name(self) -> str: ...
    @staticmethod
    def load(
        path: str, object: typing.Optional[GObject.Object] = None
    ) -> list[UnicodeData]: ...
    @staticmethod
    def load_async(
        path: str,
        object: typing.Optional[GObject.Object],
        cancellable: typing.Optional[Gio.Cancellable],
        callback: typing.Callable[..., None],
        *user_data: typing.Any,
    ) -> None: ...
    @staticmethod
    def save(path: str, list: list[UnicodeData]) -> None: ...
    def set_block_name(self, block_name: str) -> None: ...

class UnicodeDataClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UnicodeDataClass()
    """

    parent: SerializableClass = ...

class UnicodeDataPrivate(GObject.GPointer): ...

class XEvent(Serializable):
    """
    :Constructors:

    ::

        XEvent(**properties)

    Object IBusXEvent

    Properties from IBusXEvent:
      version -> guint: version
        version
      event-type -> gint: event type
        event type
      window -> guint: window
        window
      send-event -> gint: send event
        send event
      serial -> gulong: serial
        serial
      time -> guint: time
        time
      state -> guint: state
        state
      keyval -> guint: keyval
        keyval
      length -> gint: length
        length
      string -> gchararray: string
        string
      hardware-keycode -> guint: hardware keycode
        hardware keycode
      group -> guint: group
        group
      is-modifier -> gboolean: is modifier
        is modifier
      root -> guint: root
        root
      subwindow -> guint: subwindow
        subwindow
      x -> gint: x
        x
      y -> gint: y
        y
      x-root -> gint: x root
        x root
      y-root -> gint: y root
        y root
      same-screen -> gboolean: same screen
        same screen
      purpose -> gchararray: purpose
        purpose

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        event_type: int
        group: int
        hardware_keycode: int
        is_modifier: bool
        keyval: int
        length: int
        purpose: str
        root: int
        same_screen: bool
        send_event: int
        serial: int
        state: int
        string: str
        subwindow: int
        time: int
        version: int
        window: int
        x: int
        x_root: int
        y: int
        y_root: int

    props: Props = ...
    parent: Serializable = ...
    priv: XEventPrivate = ...
    event_type: XEventType = ...
    window: int = ...
    send_event: int = ...
    serial: int = ...
    def __init__(
        self,
        event_type: int = ...,
        group: int = ...,
        hardware_keycode: int = ...,
        is_modifier: bool = ...,
        keyval: int = ...,
        length: int = ...,
        purpose: str = ...,
        root: int = ...,
        same_screen: bool = ...,
        send_event: int = ...,
        serial: int = ...,
        state: int = ...,
        string: str = ...,
        subwindow: int = ...,
        time: int = ...,
        window: int = ...,
        x: int = ...,
        x_root: int = ...,
        y: int = ...,
        y_root: int = ...,
    ) -> None: ...
    def get_event_type(self) -> XEventType: ...
    def get_group(self) -> int: ...
    def get_hardware_keycode(self) -> int: ...
    def get_is_modifier(self) -> bool: ...
    def get_keyval(self) -> int: ...
    def get_length(self) -> int: ...
    def get_purpose(self) -> str: ...
    def get_root(self) -> int: ...
    def get_same_screen(self) -> bool: ...
    def get_send_event(self) -> int: ...
    def get_serial(self) -> int: ...
    def get_state(self) -> int: ...
    def get_string(self) -> str: ...
    def get_subwindow(self) -> int: ...
    def get_time(self) -> int: ...
    def get_version(self) -> int: ...
    def get_window(self) -> int: ...
    def get_x(self) -> int: ...
    def get_x_root(self) -> int: ...
    def get_y(self) -> int: ...
    def get_y_root(self) -> int: ...

class XEventClass(GObject.GPointer):
    """
    :Constructors:

    ::

        XEventClass()
    """

    parent: SerializableClass = ...
    pdummy: list[None] = ...

class XEventPrivate(GObject.GPointer): ...

class XML(GObject.GBoxed):
    """
    :Constructors:

    ::

        XML()
    """

    name: str = ...
    text: str = ...
    attributes: str = ...
    sub_nodes: list[None] = ...
    def copy(self) -> XML: ...
    def free(self) -> None: ...
    def output(self, output: GLib.String) -> None: ...
    @staticmethod
    def parse_buffer(buffer: str) -> XML: ...
    @staticmethod
    def parse_file(name: str) -> XML: ...

class BusNameFlag(GObject.GFlags):
    ALLOW_REPLACEMENT = 1
    DO_NOT_QUEUE = 4
    REPLACE_EXISTING = 2

class Capabilite(GObject.GFlags):
    AUXILIARY_TEXT = 2
    FOCUS = 8
    LOOKUP_TABLE = 4
    OSK = 64
    PREEDIT_TEXT = 1
    PROPERTY = 16
    SURROUNDING_TEXT = 32
    SYNC_PROCESS_KEY = 128
    SYNC_PROCESS_KEY_V2 = 128

class InputHints(GObject.GFlags):
    EMOJI = 512
    INHIBIT_OSK = 128
    LOWERCASE = 8
    NONE = 0
    NO_EMOJI = 1024
    NO_SPELLCHECK = 2
    PRIVATE = 2048
    SPELLCHECK = 1
    UPPERCASE_CHARS = 16
    UPPERCASE_SENTENCES = 64
    UPPERCASE_WORDS = 32
    VERTICAL_WRITING = 256
    WORD_COMPLETION = 4

class ModifierType(GObject.GFlags):
    BUTTON1_MASK = 256
    BUTTON2_MASK = 512
    BUTTON3_MASK = 1024
    BUTTON4_MASK = 2048
    BUTTON5_MASK = 4096
    CONTROL_MASK = 4
    FORWARD_MASK = 33554432
    HANDLED_MASK = 16777216
    HYPER_MASK = 134217728
    IGNORED_MASK = 33554432
    LOCK_MASK = 2
    META_MASK = 268435456
    MOD1_MASK = 8
    MOD2_MASK = 16
    MOD3_MASK = 32
    MOD4_MASK = 64
    MOD5_MASK = 128
    MODIFIER_MASK = 1593843711
    RELEASE_MASK = 1073741824
    SHIFT_MASK = 1
    SUPER_MASK = 67108864

class ObjectFlags(GObject.GFlags):
    DESTROYED = 2
    IN_DESTRUCTION = 1
    RESERVED_1 = 4
    RESERVED_2 = 8

class AttrPreedit(GObject.GEnum):
    DEFAULT = 0
    ERROR_COMPOSE = 8
    ERROR_SPELLING = 7
    NONE = 1
    PREDICTION = 4
    PREFIX = 5
    SELECTION = 3
    SUFFIX = 6
    WHOLE = 2

class AttrType(GObject.GEnum):
    BACKGROUND = 3
    FOREGROUND = 2
    UNDERLINE = 1

class AttrUnderline(GObject.GEnum):
    DOUBLE = 2
    ERROR = 4
    LOW = 3
    NONE = 0
    SINGLE = 1
    @staticmethod
    def new(underline_type: int, start_index: int, end_index: int) -> Attribute: ...

class BusGlobalBindingType(GObject.GEnum):
    ANY = 0
    EMOJI_TYPING = 2
    IME_SWITCHER = 1

class BusRequestNameReply(GObject.GEnum):
    ALREADY_OWNER = 4
    EXISTS = 3
    IN_QUEUE = 2
    PRIMARY_OWNER = 1

class BusStartServiceByNameReply(GObject.GEnum):
    ALREADY_RUNNING = 2
    SUCCESS = 1

class Error(GObject.GEnum):
    FAILED = 2
    NO_CONFIG = 1
    NO_ENGINE = 0
    @staticmethod
    def quark() -> int: ...

class InputPurpose(GObject.GEnum):
    ALPHA = 1
    DIGITS = 2
    EMAIL = 6
    FREE_FORM = 0
    NAME = 7
    NUMBER = 3
    PASSWORD = 8
    PHONE = 4
    PIN = 9
    TERMINAL = 10
    URL = 5

class Orientation(GObject.GEnum):
    HORIZONTAL = 0
    SYSTEM = 2
    VERTICAL = 1

class PreeditFocusMode(GObject.GEnum):
    CLEAR = 0
    COMMIT = 1

class PropState(GObject.GEnum):
    CHECKED = 1
    INCONSISTENT = 2
    UNCHECKED = 0

class PropType(GObject.GEnum):
    MENU = 3
    NORMAL = 0
    RADIO = 2
    SEPARATOR = 4
    TOGGLE = 1

class XEventType(GObject.GEnum):
    EVENT_LAST = 3
    KEY_PRESS = 0
    KEY_RELEASE = 1
    NOTHING = -1
    OTHER = 2
