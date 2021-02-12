# A-B-Test
İş Problemi:
Facebook kısa süre önce mevcut "maximum bidding (maksimum teklif verme)" adı verilen teklif verme türüne alternatif olarak yeni bir teklif türü olan "average bidding (ortalama teklif verme)" i tanıttı. Müşterilerimizden biri olan bombabomba.com, bu yeni özelliği test etmeye karar verdi ve average bidding'in, maximum bidding'den daha fazla dönüşüm getirip getirmediğini anlamak için bir A/B testi yapmak istiyor.

AB TEST:
Bu A/B testinde, bombabomba.com hedef kitlesini rastgele eşit büyüklükte iki gruba ayırır. Kontrol ve Test grubu. "maximum bidding" olan bir Facebook reklam kampanyası "Control Group"a sunulur ve "average bidding" olan başka bir kampanya "Test Group" a sunulur.

Müşteri yolculuğu:
Kullanıcı bir reklam görür(Impression)
Kullanıcı reklamdaki web sitesi bağlantısına tıklar (Website Click)
Kullanıcı web sitesinde arama yapar(Search)
Kullanıcı bir ürünün ayrıntılarını görüntüler (View Content)
Kullanıcı ürünü sepete ekler(Add to Cart)
Kullanıcı ürünü satın alır(Purchase)

Amaç:
A/B testi 1 aydır devam ediyor ve bombabomba.com şimdi sizden bu A/B testinin sonuçlarını analiz etmenizi bekliyor. Bombabomba.com için nihai başarı ölçütü Purchase (Satın Alma Sayısı)'dır. Bu nedenle, istatistiksel testler için purchase metriğine odaklanmalısınız.
Projeye başlarken ilk olarak gerekli kütüphaneleri import edip, kullanıcıları df_control ve df_test olarak iki grupta değerlendirdik ve veri setimizi okuttuk.
