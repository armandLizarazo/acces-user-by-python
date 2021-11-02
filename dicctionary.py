crg001 = {'Referencia': 'blkv8', 'Producto': 'Cargador ', 'Marca': 'Belkin ', 'Tipo': 'V8 ', 'Amperaje': '2.1 mah ', 'Precio ': 19000}
crg002= {'Referencia': 'blktc', 'Producto': 'Cargador ', 'Marca': 'Belkin ', 'Tipo': 'TC ', 'Amperaje': '3.1 mah ', 'Precio ': 17000}
crg003 = {'Referencia': 'nsuv8', 'Producto': 'Cargador ', 'Marca': 'Naisu ', 'Tipo': 'V8 ', 'Amperaje': '2.4 mah ', 'Precio ': 15000}
consulta = {input('Digite el codigo a consultar...')}
if (consulta == crg001):
  for i in crg001.values():
    print(f'{crg001}')
else:
  for i in crg002.values():
    print(f"{crg002}")



# if (consulta == "codigo1"):
#   for i in crg001.values():
#     print(i)
#   else:
#     for i in crg002.values(): 
#       print(i)

# for r in crg002.values():
#   return(r)
  
