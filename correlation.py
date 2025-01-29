import acipy.stats as stats
 s1=[300,301,315,321,334,400]
 s2=[202,217,229,290,289,500]
 s1,s2=stats.ttest_ind_from_stats(s1,s2)
 print(s1)
 print(s2)