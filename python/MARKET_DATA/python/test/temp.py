from _const import *
from datetime import date
import matplotlib.pyplot as plt
import numpy as np

# 从当天开始往前查询多少天的

query_day_nums = 10000
begin = TODAY - query_day_nums


def get_dayK_list(param_list):
    api_url = get_api_url(param_list=param_list)
    data_in_json = request_api(api_url=api_url)

    code = data_in_json['code']

    dayK_data_lists = data_in_json['kline']
    # print(dayK_data_lists)
    dayK_list = []
    for a_dayK_data_list in dayK_data_lists:
        a_dayK_data_dict = parse_one_dayK_data_list(a_dayK_data_list)
        a_dayK_data_dict['code'] = code
        dayK_list.append(get_one_dayK_instance(a_dayK_data_dict))

    return dayK_list


def plot_average(dayK_list: list[DayK]):
    dates = np.array([dayK.date for dayK in dayK_list])
    average_price = np.array([dayK.average for dayK in dayK_list])
    print(dates)
    print(average_price.max())

    plt.plot(dates, average_price, label='Average Prices')

    plt.legend()

    plt.xlabel('Date')
    plt.ylabel('Average Price')

    plt.show()


def main():
    param_list = {
        "begin": str(begin),
        "end": str(TODAY)
    }
    dayK_list = get_dayK_list(param_list=param_list)
    plot_average(dayK_list=dayK_list)
    ...


if __name__ == '__main__':
    main()
