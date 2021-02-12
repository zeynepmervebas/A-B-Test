# AB Testing
# parametrik - nonparametrik
# mean - medyan

# 1.1 Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi (parametrik test)
# 1.2 Varsayımlar sağlanmıyorsa mannwhitneyu testi (non-parametrik test)

# Eger normallik sağlanır varyans homojenliği sağlanmazsa ne olacak?
# T test fonksiyonuna arguman gireceğiz.

# Eğer normallik sağlanmazsa her türlü nonparametrik test yapacağız.

# H0: M1 = M2 (... iki grup ortalamaları arasında ist ol.anl.fark yoktur.)
# H1: M1 != M2 (...vardır)

# Cevaplanması Gereken Sorular :
# Bu A / B testinin hipotezini nasıl tanımlarsınız?
# İstatistiksel olarak anlamlı sonuçlar çıkarabilir miyiz?
# Hangi testi kullandınız? Neden?
# Soru 2'ye verdiğiniz cevaba göre, müşteriye tavsiyeniz nedir?

# Sampling

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro
import scipy.stats as stats

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df_control = pd.read_excel("ab_testing_data.xlsx",sheet_name="Control Group")
df_control.head()

df_test = pd.read_excel("ab_testing_data.xlsx",sheet_name="Test Group")
df_test.head()

df_control.shape
df_test.shape

# Aykırı değerler için eşik değeri belirleme
def outlier_thresholds(dataframe, variable, low_quantile=0.05, up_quantile=0.95):
    quantile_one = dataframe[variable].quantile(low_quantile)
    quantile_three = dataframe[variable].quantile(up_quantile)
    interquantile_range = quantile_three - quantile_one
    up_limit = quantile_three + 1.5 * interquantile_range
    low_limit = quantile_one - 1.5 * interquantile_range
    return low_limit, up_limit


# Değişkende herhangi bir aykırı değer olup olmadığını kontrol ediyor.
def has_outliers(dataframe, numeric_columns):
    for col in numeric_columns:
        low_limit, up_limit = outlier_thresholds(dataframe, col)
        if dataframe[(dataframe[col] > up_limit) | (dataframe[col] < low_limit)].any(axis=None):
            number_of_outliers = dataframe[(dataframe[col] > up_limit) | (dataframe[col] < low_limit)].shape[0]
            print(col, " : ", number_of_outliers, "outliers")

#aykırı değer kontrolleri
for var in df_control:
    print(var, "has " , has_outliers(df_control, [var]),  "Outliers")

for var in df_test:
    print(var, "has " , has_outliers(df_test, [var]),  "Outliers")

# Bu A / B testinin hipotezini nasıl tanımlarsınız?

#HO: kontrol ve test grupları arasında -ortalama satın alma sayısı bakımından-  istatiksel olarak farklılık yoktur.
#H1: kontrol ve test grupları arasında -ortalama satın alma sayısı bakımından- istatiksel olarak farklılık vardır.

df_control["Purchase"].mean() #550.8940587702316
df_test["Purchase"].mean() #582.1060966484675

Group_A=df_control["Purchase"]
Group_B=df_test["Purchase"]

# 1. Varsayım Kontrolü
############################

# 1.1 Normallik Varsayımı
# 1.2 Varyans Homojenliği

############################
# 1.1 Normallik Varsayımı
############################

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:..sağlanmamaktadır.

from scipy.stats import shapiro

test_istatistigi, pvalue = shapiro(Group_A)
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))

pvalue < 0.05

#Group_A normal dağılmaktadır.

test_istatistigi, pvalue = shapiro(Group_B)
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))


pvalue < 0.05

# Group_B normal dağılmaktadır.

#varyans testi

from scipy import stats
stats.levene(Group_A,Group_B)
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))

# 1.1 Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi (parametrik test)
test_istatistigi, pvalue = stats.ttest_ind(Group_A,Group_B,
                                           equal_var=True)
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))

# İstatistiksel olarak anlamlı sonuçlar çıkarabilir miyiz?
#Kontrol ve test grubu arasında istatiksel bir fark yoktur.

# Hangi testi kullandınız? Neden?
#varsayımlar sağlandığı için iki örneklem ttest kullandık.

# Soru 2'ye verdiğiniz cevaba göre, müşteriye tavsiyeniz nedir?
#average veya maximum bidding arasında çok fark yoktur.iki yöntemden biri seçilebilir.
#gözlem sayısı arttırılabilir.
#test süresi uzatılabilir.





