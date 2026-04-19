REPORT z_o2c_report.

TABLES: vbak, vbap.

SELECT vbak~vbeln, vbak~kunnr, vbap~matnr, vbap~kwmeng
  INTO TABLE @DATA(result)
  FROM vbak
  INNER JOIN vbap
  ON vbak~vbeln = vbap~vbeln.

LOOP AT result INTO DATA(row).
  WRITE: / 'Order:', row-vbeln,
           'Customer:', row-kunnr,
           'Material:', row-matnr,
           'Qty:', row-kwmeng.
ENDLOOP.