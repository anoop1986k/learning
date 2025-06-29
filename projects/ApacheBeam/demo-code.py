import apache_beam as beam

def SplitRow(element):
    return element.split(',')

def filtering(record):
  return record[3] == 'HR'


p1 = beam.Pipeline()

attendance_count = (
    
   p1
    |beam.io.ReadFromText('dept_data.txt')
    |beam.Map(SplitRow)
   #| beam.Map(lambda record: record.split(','))

    |beam.Filter(filtering)
  # |beam.Filter(lambda record: record[3] == 'Accounts')
    
    |beam.Map(lambda record: (record[1], 1))
    |beam.CombinePerKey(sum)
    
    |beam.io.WriteToText('data/output_new_final')
  
)

p1.run()