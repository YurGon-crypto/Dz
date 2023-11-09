class Mathematician:
    def square_nums(self, num_list):
        return [num**2 for num in num_list]


    def remove_positives(self, num_list):
        return [num for num in num_list if num <= 0]


    def filter_leaps(self, year_list):
        return [year for year in year_list if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
