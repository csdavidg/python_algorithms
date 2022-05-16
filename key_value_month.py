from datetime import date
import calendar

month_length = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

key_array   = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July',
                'August', 'September', 'October', 'November', 'December' ]

idx = key_array.index('February')
print('February has', month_length[idx], 'days')

def print_month(month, year):
  idx = key_array.index(month)                
  day = 1

  wd = date(year,idx + 1,day).weekday()       
  wd = (wd + 1) % 7                           
  end = month_length[idx]                     
  if calendar.isleap(year) and idx == 1:      
    end += 1

  print('{} {}'.format(month,year).center(20))
  print('Su Mo Tu We Th Fr Sa')
  print('   ' * wd, end='')
  while day <= end:
    print('{:2d} '.format(day), end='')
    wd = (wd + 1) % 7
    day += 1
    if wd == 0: print()                       
  print()