import pandas as pd
import numpy as np
df = pd.read_excel('CourseOutcomes.xlsx')

df['Dept'] = [x.split(':')[0].split(' ')[0] for x in df['Class']]
df['Course Num'] = [x.split(':')[0].split(' ')[1] for x in df['Class']]
print (df['Dept'].unique())

for dept, groupDf in df.groupby('Dept'):
	groupDf['Years'].fillna(method='ffill', inplace=True)
	new_df = pd.DataFrame(groupDf['Class'].unique())
	new_df.columns = ['Class']
	other_df = pd.DataFrame({
			'Class':'{} 23: INDEPENDENT STUDY'.format(dept),
			'Class':'{} 22: FIELD WORK AND SERV'.format(dept),
		},index=[0])
	third_df = pd.DataFrame({'Class':None}, index=range(20))
	third_df['Class'] = [None]*20
	
	for col in ['PROGRAM OUTCOMES ARE LISTED IN BANNER ON THE GAVILAN WEBPAGE','COURSE LEVEL SLOs ARE LISTED IN BANNER', 'SLO ASSESSMENT OR MEASUREMENT METHODS ARE LISTED', 'SLOs ARE ASSESSED', 'EACH SLO ASSESSMENT HAS AT LEAST TWO SENTENCES IN THE "ASSESSED" SECTION', 'EVIDENCE OF USE OF RESULTS ARE LISTED', 'NOT EVERY SLO THAT IS LISTED IS ASSESSED', 'SLO BOXES ARE NOT AVAILABLE: NO DATA COLLECTED ON SPECIFIC COURSE',	'LAST YEAR ASSESSED AS OF DEC. 2018', 'PERCENTAGE OF COURSE THAT HAVE BEEN FULLY ASSESSED WITHIN LAST 4 YEARS']:
		col = col.split(' ')
		i = 5
		while i < len(col):
			col.insert(i, '\n')
			i += (5+1)
		col = ' '.join(col)

		new_df[col] = np.nan
		other_df[col] = np.nan
		
	new_df = pd.concat([new_df, other_df])
	
	new_df['Course Num'] = ['{}'.format(x.split(':')[0].split(' ')[1]) for x in new_df['Class']]
	string = new_df['Course Num'].values

	new_num = []
	new_letter = []
	for val in string:
		try:
			new_num.append(int(val))
			new_letter.append('')
		except:
			new_num.append(int(val[:-1]))
			new_letter.append(val[-1])

	new_df['Course Num'] = new_num
	new_df['Course Letter'] = new_letter

	new_df.sort_values(by=['Course Num', 'Course Letter'], inplace=True)
	new_df.reset_index(drop=True, inplace=True)
	new_df.drop(['Course Num','Course Letter'], axis=1, inplace=True)	
	new_df = pd.concat([new_df, third_df])
	new_df.reset_index(drop=True, inplace=True)
	cols = list(new_df.columns.values)
	cols.pop(cols.index('Class'))
	cols = ['Class'] + cols

	new_df = new_df.loc[:,cols]
	writer = pd.ExcelWriter('split_excel/{}.xlsx'.format(dept))

	new_df.to_excel(writer,'Sheet1')

	workbook = writer.book
	worksheet = writer.sheets['Sheet1']
	
	format1 = workbook.add_format({
        'text_wrap':True,
        'align':'center'
    })
    
	format0 = workbook.add_format({'bg_color': 'red'})

	worksheet.set_column('A:A', 15, format1)
	worksheet.set_row(0, None, format1)
	worksheet.set_column('B:L', 50, format1)

	abc = workbook.add_format({'bg_color': '#FFC7CE',
							   'font_color': '#9C0006'})
	worksheet.conditional_format(1, 2, 1000, 6,
							 {'type': 'blanks',
							 'format': abc})

	writer.save()

df2 = pd.read_excel('split_excel/HIST.xlsx')
# print (df2)
