# coding=utf-8
import csv
import getpass
import os.path

from logger import logger_object
from test.GoogleSearchPageTest import GoogleSearchPageTest


def run_test(f_path):
    run_counter = 0
    list_of_second_chrome = []
    list_of_second_edge = []
    list_of_second_ie = []
    list_of_second_opera = []
    list_of_second_firefox = []

    write_log = logger_object.get_instance()
    try:
        if os.path.exists(f_path):
            ignore_line_number = 1
            search_text_col = 1
            with open(f_path) as file_object:
                mycsv = csv.reader(file_object, delimiter=',')
                mycsv = list(mycsv)
                for row in mycsv[ignore_line_number:]:  # skip 1st element
                    write_log.info("Run:{} | Keyword: {}".format(run_counter, row[search_text_col]))
                    run_counter += 1
                    time_chrome, time_edge, time_ie, time_opera, time_firefox = test_browser_search(
                        row[search_text_col])  # pick search text from 2nd row
                    if time_chrome:
                        list_of_second_chrome.append(time_chrome)
                    if time_edge:
                        list_of_second_edge.append(time_edge)
                    if time_ie:
                        list_of_second_ie.append(time_ie)
                    if time_opera:
                        list_of_second_opera.append(time_opera)
                    if time_firefox:
                        list_of_second_firefox.append(time_firefox)
        else:
            run_counter += 1
            print "Run: {} | Keyword: {}".format(run_counter, f_path)
            write_log.info("Run: {} | Keyword: {}".format(run_counter, f_path))
            time_chrome, time_edge, time_ie, time_opera, time_firefox = test_browser_search(f_path)
            if time_chrome:
                list_of_second_chrome.append(time_chrome)
            if time_edge:
                list_of_second_edge.append(time_edge)
            if time_ie:
                list_of_second_ie.append(time_ie)
            if time_opera:
                list_of_second_opera.append(time_opera)
            if time_firefox:
                list_of_second_firefox.append(time_firefox)
    except Exception as err:
        write_log.error(err)
    finally:
        write_log.info("*" * 30)
        write_log.info("Total search strings: {}".format(run_counter))
        write_log.info("Run: {} | Keyword: {}".format(run_counter, f_path))
        get_browser_performance("Chrome ", list_of_second_chrome)
        get_browser_performance("Edge   ", list_of_second_edge)
        # get_browser_performance("IE     ", list_of_second_edge)
        get_browser_performance("Opera  ", list_of_second_edge)
        get_browser_performance("Firefox", list_of_second_edge)
        write_log.info("*" * 30)


def get_browser_performance(browser_name, list_of_second_chrome):
    write_log = logger_object.get_instance()
    try:
        write_log.info(
            "Browser: {} | Successful searches: {} | Avg Time (sec): {}".format(browser_name, len(list_of_second_chrome),
                                                                       sum(list_of_second_chrome) / len(
                                                                           list_of_second_chrome)))
    except ZeroDivisionError:
        write_log.error("Browser: {} | search count is Zero".format(browser_name))


def test_browser_search(text):
    time_chrome = time_edge = time_ie = time_opera = time_firefox = None
    google_search_page_test = GoogleSearchPageTest(search_text=text)
    time_chrome = google_search_page_test.run_on_chrome()
    time_edge = google_search_page_test.run_on_edge()
    # time_ie = google_search_page_test.run_on_ie()
    time_opera = google_search_page_test.run_on_opera()
    time_firefox = google_search_page_test.run_on_firefox()
    return time_chrome, time_edge, time_ie, time_opera, time_firefox


if __name__ == '__main__':
    print('Hi, {}!'.format(getpass.getuser()))  # Press Ctrl+F8 to toggle the breakpoint.
    search_text = "women’s world cup 2019"
    file2 = r"repo\l1.csv"
    file_path = r"repo\Top 100 Google search queries in the US (as of 2020).csv"
    run_test(f_path=file_path)
    # run_test(search_text)
