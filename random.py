def count_in_time(n):
 import time
 count = 0
 start_time = time.clock()
 end_time = start_time + n
 while start_time < end_time:
     count += 1
     start_time += (time.clock() - start_time)
 return count


def generate_random(time_to_count, range_nums, rand_lst_size):
  randoms = []
  iterables = range(range_nums)
  count = 0
  for i in range(rand_lst_size):
      count += count_in_time(time_to_count)
      randoms.append(iterables[count%len(iterables)])
  return randoms
