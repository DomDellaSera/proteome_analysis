#
#
#
#This file is redundant and it is made to be so. These functions serve as
# cached constants that are called by unittests.py. 


def getPandaRow():
    import numpy as np
    row = np.array([[1, 100.0, 'A8NJZ7', 1, 1, 122]], dtype=object)
    return(row)

def getHeaders():

    headers = ['>sp|P90689|ACT_BRUMA Actin OS=Brugia malayi PE=1 SV=1', '>sp|A8Q3T2|ASNA_BRUMA ATPase ASNA1 homolog OS=Brugia malayi GN=Bm1_42140 PE=3 SV=1', '>sp|A8PWB6|BOP1_BRUMA Ribosome biogenesis protein BOP1 homolog OS=Brugia malayi GN=Bm1_36175 PE=3 SV=1', '>sp|P29030|CHIT_BRUMA Endochitinase OS=Brugia malayi PE=1 SV=1', '>sp|A8PB32|CLP1_BRUMA Protein CLP1 homolog OS=Brugia malayi GN=Bm1_20975 PE=3 SV=1', '>sp|A8PJX4|CLU_BRUMA Clustered mitochondria protein homolog OS=Brugia malayi GN=Bm1_28595 PE=3 SV=2', '>sp|A8QFY9|DDRGK_BRUMA DDRGK domain-containing protein 1 OS=Brugia malayi GN=Bm1_54325 PE=3 SV=1', '>sp|Q27450|CYP1_BRUMA Peptidyl-prolyl cis-trans isomerase 1 OS=Brugia malayi GN=CYP-1 PE=1 SV=1', '>sp|A8QBB1|DRE2_BRUMA Anamorsin homolog OS=Brugia malayi GN=Bm1_48140 PE=3 SV=1', '>sp|A8QDN3|EIF3K_BRUMA Eukaryotic translation initiation factor 3 subunit K OS=Brugia malayi GN=Bm1_52955 PE=3 SV=1', '>sp|A8PHP4|EIF3L_BRUMA Eukaryotic translation initiation factor 3 subunit L OS=Brugia malayi GN=Bm1_25770 PE=3 SV=1', '>sp|A8QE76|EFTS_BRUMA Elongation factor Ts, mitochondrial OS=Brugia malayi GN=Bm1_50845 PE=3 SV=1', '>sp|A8PKH2|EIF3A_BRUMA Eukaryotic translation initiation factor 3 subunit A OS=Brugia malayi GN=Bm1_29045 PE=3 SV=1', '>sp|A8NY27|EIF3E_BRUMA Eukaryotic translation initiation factor 3 subunit E OS=Brugia malayi GN=Bm1_11985 PE=3 SV=2', '>sp|A8NS61|EIF3G_BRUMA Eukaryotic translation initiation factor 3 subunit G OS=Brugia malayi GN=Bm1_08615 PE=3 SV=1', '>sp|A8QCY3|EIF3H_BRUMA Eukaryotic translation initiation factor 3 subunit H OS=Brugia malayi GN=Bm1_50170 PE=3 SV=1', '>sp|A8QBF3|EIF3I_BRUMA Eukaryotic translation initiation factor 3 subunit I OS=Brugia malayi GN=Bm1_48300 PE=3 SV=1', '>sp|Q4VWF8|GPMI_BRUMA 2,3-bisphosphoglycerate-independent phosphoglycerate mutase OS=Brugia malayi GN=ipgm-1 PE=1 SV=1', '>sp|P67877|GPXC_BRUMA Cuticular glutathione peroxidase OS=Brugia malayi PE=1 SV=1', '>sp|A8NS89|GOB1_BRUMA Trehalose-phosphatase OS=Brugia malayi GN=Bm1_08695 PE=1 SV=1', '>sp|A8QCH0|FEN1_BRUMA Flap endonuclease 1 OS=Brugia malayi GN=FEN1 PE=3 SV=1', '>sp|Q93142|FAR1_BRUMA Fatty-acid and retinol-binding protein 1 OS=Brugia malayi GN=far-1 PE=1 SV=1', '>sp|A8QGZ7|FBSP1_BRUMA F-box/SPRY domain-containing protein 1 OS=Brugia malayi GN=Bm1_56115 PE=3 SV=1', '>sp|P48812|G3P_BRUMA Glyceraldehyde-3-phosphate dehydrogenase OS=Brugia malayi GN=G3PD PE=1 SV=1', '>sp|A8PJJ2|GATC_BRUMA Glutamyl-tRNA(Gln) amidotransferase subunit C, mitochondrial OS=Brugia malayi GN=Bm1_27920 PE=3 SV=1', '>sp|A8QCE7|GUF1_BRUMA Translation factor GUF1 homolog, mitochondrial OS=Brugia malayi GN=Bm1_49530 PE=3 SV=1', '>sp|P27541|HSP70_BRUMA Heat shock 70 kDa protein OS=Brugia malayi GN=HSP70 PE=3 SV=1', '>sp|A0A0K0JFP3|HXK_BRUMA Hexokinase OS=Brugia malayi GN=Bm4678 PE=1 SV=1', '>sp|A8PGQ3|NARF_BRUMA Probable cytosolic Fe-S cluster assembly factor Bm1_25010 OS=Brugia malayi GN=Bm1_25010 PE=3 SV=1', '>sp|Q01202|MYSP_BRUMA Paramyosin OS=Brugia malayi PE=2 SV=2', '>sp|P48817|NDK_BRUMA Nucleoside diphosphate kinase OS=Brugia malayi GN=NDK PE=2 SV=1', '>sp|A8PV03|SLX1_BRUMA Structure-specific endonuclease subunit SLX1 homolog OS=Brugia malayi GN=Bm1_35165 PE=3 SV=1', '>sp|A8QFF6|SPAST_BRUMA Probable spastin homolog Bm1_53365 OS=Brugia malayi GN=Bm1_53365 PE=3 SV=1', '>sp|A8NJZ7|SCOC_BRUMA Short coiled-coil protein homolog OS=Brugia malayi GN=Bm1_04115 PE=3 SV=1', '>sp|P90703|RLA2_BRUMA 60S acidic ribosomal protein P2 OS=Brugia malayi GN=rpp-2 PE=3 SV=1', '>sp|P90707|RS23_BRUMA 40S ribosomal protein S23 OS=Brugia malayi GN=rps-23 PE=2 SV=1', '>sp|A8PJ38|RS3A_BRUMA 40S ribosomal protein S3a OS=Brugia malayi GN=Bm1_27225 PE=3 SV=1', '>sp|A8Q2H5|RSSA_BRUMA 40S ribosomal protein SA OS=Brugia malayi GN=Bm1_41245 PE=3 SV=2', '>sp|A8QC60|RTCB_BRUMA tRNA-splicing ligase RtcB homolog OS=Brugia malayi GN=Bm1_49220 PE=3 SV=1', '>sp|P90697|TCTP_BRUMA Translationally-controlled tumor protein homolog OS=Brugia malayi PE=2 SV=1', '>sp|P48822|TDX1_BRUMA Thioredoxin peroxidase 1 OS=Brugia malayi GN=TSA1 PE=2 SV=1', '>sp|Q17172|TDX2_BRUMA Thioredoxin peroxidase 2 OS=Brugia malayi GN=tsa-2 PE=2 SV=2', '>sp|P10723|SYNC_BRUMA Asparagine--tRNA ligase, cytoplasmic OS=Brugia malayi PE=1 SV=1', '>sp|Q9Y193|TIM13_BRUMA Mitochondrial import inner membrane translocase subunit Tim13 OS=Brugia malayi GN=TIM13 PE=3 SV=1', '>sp|A8NFF0|TRMB_BRUMA tRNA (guanine-N(7)-)-methyltransferase OS=Brugia malayi GN=Bm1_01445 PE=3 SV=1', '>sp|A8Q8J2|UFC1_BRUMA Ubiquitin-fold modifier-conjugating enzyme 1 OS=Brugia malayi GN=Bm1_46190 PE=3 SV=1', '>sp|A8Q8M5|UFM1_BRUMA Ubiquitin-fold modifier 1 OS=Brugia malayi GN=Bm1_46275 PE=3 SV=1', '>sp|A8Q2R5|WDR48_BRUMA WD repeat-containing protein 48 homolog OS=Brugia malayi GN=Bm1_41555 PE=3 SV=2', '>sp|Q17162|VINC_BRUMA Vinculin OS=Brugia malayi PE=2 SV=1', '>sp|A8QB65|WDR12_BRUMA Ribosome biogenesis protein WDR12 homolog OS=Brugia malayi GN=Bm1_47965 PE=3 SV=1', '>sp|O77049|JTB_BRUMA Protein JTB OS=Brugia malayi GN=JTB PE=2 SV=1', '>sp|A8PF69|LIAS_BRUMA Lipoyl synthase, mitochondrial OS=Brugia malayi GN=Bm1_23910 PE=3 SV=1', '>sp|A8QCE4|LST2_BRUMA Lateral signaling target protein 2 homolog OS=Brugia malayi GN=Bm1_49520 PE=3 SV=1', '>sp|P91850|MIFH_BRUMA Macrophage migration inhibitory factor homolog OS=Brugia malayi GN=Bm1_28435 PE=3 SV=4', '>sp|A8PW87|NUBP1_BRUMA Cytosolic Fe-S cluster assembly factor NUBP1 homolog OS=Brugia malayi GN=Bm1_36105 PE=3 SV=1', '>sp|A8QFQ3|NO66_BRUMA Bifunctional lysine-specific demethylase and histidyl-hydroxylase NO66 OS=Brugia malayi GN=Bm1_53875 PE=3 SV=1', '>sp|A8QHQ0|PESC_BRUMA Pescadillo homolog OS=Brugia malayi GN=Bm1_57380 PE=3 SV=2', '>sp|Q8IHI1|PSF2_BRUMA Probable DNA replication complex GINS protein PSF2 OS=Brugia malayi GN=BMBAC01P19.06 PE=3 SV=1', '>sp|A8QE42|PURA_BRUMA Adenylosuccinate synthetase OS=Brugia malayi GN=Bm1_50695 PE=3 SV=1', '>sp|P38542|RAN_BRUMA GTP-binding nuclear protein Ran OS=Brugia malayi GN=Bm1_44725 PE=2 SV=2', '>sp|Q93140|RL23_BRUMA 60S ribosomal protein L23 OS=Brugia malayi GN=RPL23 PE=2 SV=1', '>sp|P90702|RL44_BRUMA 60S ribosomal protein L44 OS=Brugia malayi GN=rpl-44 PE=3 SV=3', '>sp|A8P7J8|U518_BRUMA UPF0518 protein Bm1_18400 OS=Brugia malayi GN=Bm1_18400 PE=3 SV=1', '>sp|A8NJ91|U729_BRUMA UPF0729 protein Bm1_03610 OS=Brugia malayi GN=Bm1_03610 PE=3 SV=1']
    return(headers)
    
    
def subsetted_Headers():
    headers = [['P90689', 'Actin', 'NaGN'], ['A8Q3T2', 'ATPase ASNA1 homolog', 'Bm1_42140'], ['A8PWB6', 'Ribosome biogenesis protein BOP1 homolog', 'Bm1_36175'], ['P29030', 'Endochitinase', 'NaGN'], ['A8PB32', 'Protein CLP1 homolog', 'Bm1_20975'], ['A8PJX4', 'Clustered mitochondria protein homolog', 'Bm1_28595'], ['A8QFY9', 'DDRGK domain-containing protein 1', 'Bm1_54325'], ['Q27450', 'Peptidyl-prolyl cis-trans isomerase 1', 'CYP-1'], ['A8QBB1', 'Anamorsin homolog', 'Bm1_48140'], ['A8QDN3', 'Eukaryotic translation initiation factor 3 subunit K', 'Bm1_52955'], ['A8PHP4', 'Eukaryotic translation initiation factor 3 subunit L', 'Bm1_25770'], ['A8QE76', 'Elongation factor Ts, mitochondrial', 'Bm1_50845'], ['A8PKH2', 'Eukaryotic translation initiation factor 3 subunit A', 'Bm1_29045'], ['A8NY27', 'Eukaryotic translation initiation factor 3 subunit E', 'Bm1_11985'], ['A8NS61', 'Eukaryotic translation initiation factor 3 subunit G', 'Bm1_08615'], ['A8QCY3', 'Eukaryotic translation initiation factor 3 subunit H', 'Bm1_50170'], ['A8QBF3', 'Eukaryotic translation initiation factor 3 subunit I', 'Bm1_48300'], ['Q4VWF8', '2,3-bisphosphoglycerate-independent phosphoglycerate mutase', 'ipgm-1'], ['P67877', 'Cuticular glutathione peroxidase', 'NaGN'], ['A8NS89', 'Trehalose-phosphatase', 'Bm1_08695'], ['A8QCH0', 'Flap endonuclease 1', 'FEN1'], ['Q93142', 'Fatty-acid and retinol-binding protein 1', 'far-1'], ['A8QGZ7', 'F-box/SPRY domain-containing protein 1', 'Bm1_56115'], ['P48812', 'Glyceraldehyde-3-phosphate dehydrogenase', 'G3PD'], ['A8PJJ2', 'Glutamyl-tRNA(Gln) amidotransferase subunit C, mitochondrial', 'Bm1_27920'], ['A8QCE7', 'Translation factor GUF1 homolog, mitochondrial', 'Bm1_49530'], ['P27541', 'Heat shock 70 kDa protein', 'HSP70'], ['A0A0K0JFP3', 'Hexokinase', 'Bm4678'], ['A8PGQ3', 'Probable cytosolic Fe-S cluster assembly factor Bm1_25010', 'Bm1_25010'], ['Q01202', 'Paramyosin', 'NaGN'], ['P48817', 'Nucleoside diphosphate kinase', 'NDK'], ['A8PV03', 'Structure-specific endonuclease subunit SLX1 homolog', 'Bm1_35165'], ['A8QFF6', 'Probable spastin homolog Bm1_53365', 'Bm1_53365'], ['A8NJZ7', 'Short coiled-coil protein homolog', 'Bm1_04115'], ['P90703', '60S acidic ribosomal protein P2', 'rpp-2'], ['P90707', '40S ribosomal protein S23', 'rps-23'], ['A8PJ38', '40S ribosomal protein S3a', 'Bm1_27225'], ['A8Q2H5', '40S ribosomal protein SA', 'Bm1_41245'], ['A8QC60', 'tRNA-splicing ligase RtcB homolog', 'Bm1_49220'], ['P90697', 'Translationally-controlled tumor protein homolog', 'NaGN'], ['P48822', 'Thioredoxin peroxidase 1', 'TSA1'], ['Q17172', 'Thioredoxin peroxidase 2', 'tsa-2'], ['P10723', 'Asparagine--tRNA ligase, cytoplasmic', 'NaGN'], ['Q9Y193', 'Mitochondrial import inner membrane translocase subunit Tim13', 'TIM13'], ['A8NFF0', 'tRNA (guanine-N(7)-)-methyltransferase', 'Bm1_01445'], ['A8Q8J2', 'Ubiquitin-fold modifier-conjugating enzyme 1', 'Bm1_46190'], ['A8Q8M5', 'Ubiquitin-fold modifier 1', 'Bm1_46275'], ['A8Q2R5', 'WD repeat-containing protein 48 homolog', 'Bm1_41555'], ['Q17162', 'Vinculin', 'NaGN'], ['A8QB65', 'Ribosome biogenesis protein WDR12 homolog', 'Bm1_47965'], ['O77049', 'Protein JTB', 'JTB'], ['A8PF69', 'Lipoyl synthase, mitochondrial', 'Bm1_23910'], ['A8QCE4', 'Lateral signaling target protein 2 homolog', 'Bm1_49520'], ['P91850', 'Macrophage migration inhibitory factor homolog', 'Bm1_28435'], ['A8PW87', 'Cytosolic Fe-S cluster assembly factor NUBP1 homolog', 'Bm1_36105'], ['A8QFQ3', 'Bifunctional lysine-specific demethylase and histidyl-hydroxylase NO66', 'Bm1_53875'], ['A8QHQ0', 'Pescadillo homolog', 'Bm1_57380'], ['Q8IHI1', 'Probable DNA replication complex GINS protein PSF2', 'BMBAC01P19.06'], ['A8QE42', 'Adenylosuccinate synthetase', 'Bm1_50695'], ['P38542', 'GTP-binding nuclear protein Ran', 'Bm1_44725'], ['Q93140', '60S ribosomal protein L23', 'RPL23'], ['P90702', '60S ribosomal protein L44', 'rpl-44'], ['A8P7J8', 'UPF0518 protein Bm1_18400', 'Bm1_18400'], ['A8NJ91', 'UPF0729 protein Bm1_03610', 'Bm1_03610']]
    return(headers)

def truncated_Headers():
    truncated_Headers = ['Actin OS=Brugia malayi PE=1 SV=1',
     ' ATPase ASNA1 homolog OS=Brugia malayi GN=Bm1_42140 PE=3 SV=1',
     ' Ribosome biogenesis protein BOP1 homolog OS=Brugia malayi GN=Bm1_36175 PE=3 SV=1',
     ' Endochitinase OS=Brugia malayi PE=1 SV=1',
     ' Protein CLP1 homolog OS=Brugia malayi GN=Bm1_20975 PE=3 SV=1',
     'Clustered mitochondria protein homolog OS=Brugia malayi GN=Bm1_28595 PE=3 SV=2',
     'A DDRGK domain-containing protein 1 OS=Brugia malayi GN=Bm1_54325 PE=3 SV=1',
     ' Peptidyl-prolyl cis-trans isomerase 1 OS=Brugia malayi GN=CYP-1 PE=1 SV=1',
     ' Anamorsin homolog OS=Brugia malayi GN=Bm1_48140 PE=3 SV=1',
     'A Eukaryotic translation initiation factor 3 subunit K OS=Brugia malayi GN=Bm1_52955 PE=3 SV=1',
     'A Eukaryotic translation initiation factor 3 subunit L OS=Brugia malayi GN=Bm1_25770 PE=3 SV=1',
     ' Elongation factor Ts, mitochondrial OS=Brugia malayi GN=Bm1_50845 PE=3 SV=1',
     'A Eukaryotic translation initiation factor 3 subunit A OS=Brugia malayi GN=Bm1_29045 PE=3 SV=1',
     'A Eukaryotic translation initiation factor 3 subunit E OS=Brugia malayi GN=Bm1_11985 PE=3 SV=2',
     'A Eukaryotic translation initiation factor 3 subunit G OS=Brugia malayi GN=Bm1_08615 PE=3 SV=1',
     'A Eukaryotic translation initiation factor 3 subunit H OS=Brugia malayi GN=Bm1_50170 PE=3 SV=1',
     'A Eukaryotic translation initiation factor 3 subunit I OS=Brugia malayi GN=Bm1_48300 PE=3 SV=1',
     ' 2,3-bisphosphoglycerate-independent phosphoglycerate mutase OS=Brugia malayi GN=ipgm-1 PE=1 SV=1',
     ' Cuticular glutathione peroxidase OS=Brugia malayi PE=1 SV=1',
     ' Trehalose-phosphatase OS=Brugia malayi GN=Bm1_08695 PE=1 SV=1',
     ' Flap endonuclease 1 OS=Brugia malayi GN=FEN1 PE=3 SV=1',
     ' Fatty-acid and retinol-binding protein 1 OS=Brugia malayi GN=far-1 PE=1 SV=1',
     'A F-box/SPRY domain-containing protein 1 OS=Brugia malayi GN=Bm1_56115 PE=3 SV=1',
     'Glyceraldehyde-3-phosphate dehydrogenase OS=Brugia malayi GN=G3PD PE=1 SV=1',
     ' Glutamyl-tRNA(Gln) amidotransferase subunit C, mitochondrial OS=Brugia malayi GN=Bm1_27920 PE=3 SV=1',
     ' Translation factor GUF1 homolog, mitochondrial OS=Brugia malayi GN=Bm1_49530 PE=3 SV=1',
     'A Heat shock 70 kDa protein OS=Brugia malayi GN=HSP70 PE=3 SV=1',
     'UMA Hexokinase OS=Brugia malayi GN=Bm4678 PE=1 SV=1',
     ' Probable cytosolic Fe-S cluster assembly factor Bm1_25010 OS=Brugia malayi GN=Bm1_25010 PE=3 SV=1',
     ' Paramyosin OS=Brugia malayi PE=2 SV=2',
     'Nucleoside diphosphate kinase OS=Brugia malayi GN=NDK PE=2 SV=1',
     ' Structure-specific endonuclease subunit SLX1 homolog OS=Brugia malayi GN=Bm1_35165 PE=3 SV=1',
     'A Probable spastin homolog Bm1_53365 OS=Brugia malayi GN=Bm1_53365 PE=3 SV=1',
     ' Short coiled-coil protein homolog OS=Brugia malayi GN=Bm1_04115 PE=3 SV=1',
     ' 60S acidic ribosomal protein P2 OS=Brugia malayi GN=rpp-2 PE=3 SV=1',
     ' 40S ribosomal protein S23 OS=Brugia malayi GN=rps-23 PE=2 SV=1',
     ' 40S ribosomal protein S3a OS=Brugia malayi GN=Bm1_27225 PE=3 SV=1',
     ' 40S ribosomal protein SA OS=Brugia malayi GN=Bm1_41245 PE=3 SV=2',
     ' tRNA-splicing ligase RtcB homolog OS=Brugia malayi GN=Bm1_49220 PE=3 SV=1',
     ' Translationally-controlled tumor protein homolog OS=Brugia malayi PE=2 SV=1',
     ' Thioredoxin peroxidase 1 OS=Brugia malayi GN=TSA1 PE=2 SV=1',
     ' Thioredoxin peroxidase 2 OS=Brugia malayi GN=tsa-2 PE=2 SV=2',
     ' Asparagine--tRNA ligase, cytoplasmic OS=Brugia malayi PE=1 SV=1',
     'A Mitochondrial import inner membrane translocase subunit Tim13 OS=Brugia malayi GN=TIM13 PE=3 SV=1',
     ' tRNA (guanine-N(7)-)-methyltransferase OS=Brugia malayi GN=Bm1_01445 PE=3 SV=1',
     ' Ubiquitin-fold modifier-conjugating enzyme 1 OS=Brugia malayi GN=Bm1_46190 PE=3 SV=1',
     ' Ubiquitin-fold modifier 1 OS=Brugia malayi GN=Bm1_46275 PE=3 SV=1',
     'A WD repeat-containing protein 48 homolog OS=Brugia malayi GN=Bm1_41555 PE=3 SV=2',
     ' Vinculin OS=Brugia malayi PE=2 SV=1',
     'A Ribosome biogenesis protein WDR12 homolog OS=Brugia malayi GN=Bm1_47965 PE=3 SV=1',
     'Protein JTB OS=Brugia malayi GN=JTB PE=2 SV=1',
     ' Lipoyl synthase, mitochondrial OS=Brugia malayi GN=Bm1_23910 PE=3 SV=1',
     ' Lateral signaling target protein 2 homolog OS=Brugia malayi GN=Bm1_49520 PE=3 SV=1',
     ' Macrophage migration inhibitory factor homolog OS=Brugia malayi GN=Bm1_28435 PE=3 SV=4',
     'A Cytosolic Fe-S cluster assembly factor NUBP1 homolog OS=Brugia malayi GN=Bm1_36105 PE=3 SV=1',
     ' Bifunctional lysine-specific demethylase and histidyl-hydroxylase NO66 OS=Brugia malayi GN=Bm1_53875 PE=3 SV=1',
     ' Pescadillo homolog OS=Brugia malayi GN=Bm1_57380 PE=3 SV=2',
     ' Probable DNA replication complex GINS protein PSF2 OS=Brugia malayi GN=BMBAC01P19.06 PE=3 SV=1',
     ' Adenylosuccinate synthetase OS=Brugia malayi GN=Bm1_50695 PE=3 SV=1',
     'GTP-binding nuclear protein Ran OS=Brugia malayi GN=Bm1_44725 PE=2 SV=2',
     ' 60S ribosomal protein L23 OS=Brugia malayi GN=RPL23 PE=2 SV=1',
     ' 60S ribosomal protein L44 OS=Brugia malayi GN=rpl-44 PE=3 SV=3',
     ' UPF0518 protein Bm1_18400 OS=Brugia malayi GN=Bm1_18400 PE=3 SV=1',
     ' UPF0729 protein Bm1_03610 OS=Brugia malayi GN=Bm1_03610 PE=3 SV=1']
    
    #truncated_Headers=[x[len('>sp|Q93142|FAR1_BRUMA'):] for x in raw_Headers]
    #formatted_Headers = [[x[1] for x in raw_Headers]]
    return(truncated_Headers)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    