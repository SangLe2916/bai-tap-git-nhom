def tinh_thue_thu_nhap(thu_nhap):
  #Dev A ap dung giam tru 4 trieu va thue 5%
  thu_nhap_tinh_thue = thu_nhap - 4000000
  return max(0,thu_nhap_tinh_thue*0.05)