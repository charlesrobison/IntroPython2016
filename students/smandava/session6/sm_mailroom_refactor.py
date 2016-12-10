#!/usr/bin/env python3
"""Nov 27 2016 Mail room Exercise refactoring for testing."""
import operator
donor_dict = {'Alfred Hitchcock': [10, 20, 30],
              'Martin Scorsese': [20, 30, 40],
              'Steven Spielberg': [40, 20, 30, 10],
              'Francis Coppola': [10, 10, 10],
              'Ridley Scott': [10, 20, 30, 10]}

donor_summary_dict = {}
donor_report = []

def print_report():
    report_header = ("{0:<30s} {1:<30s} {2:<30s} {3:<30s}".
                     format('Donor Name',
                            'Total Amount', 'No.of Donations',
                            'Avg.Donation'))


    donor_summary_dict = {donorname: [sum(donor_dict[donorname]), len(donor_dict[donorname]), (sum(donor_dict[donorname]) / len(donor_dict[donorname]))] for donorname in donor_dict.keys()}
    sorted_donors = sorted(donor_summary_dict.items(),
                           key=operator.itemgetter(1), reverse=True)
    for donor in (sorted_donors):
        donor_report.append(donor[0] + ' ' + str(donor[1][0]) + ' ' + str(donor[1][1]) + ' ' + str(donor[1][2]))
    return "\n".join(donor_report)


def send_thanks(user_input, d_amount=None):
    if (user_input == 'list'):
        return(donor_dict)
    if user_input in donor_dict.keys():
        try:
            d_amount = int(d_amount)
        except ValueError as error:
            return (type(error).__name__)
        donor_dict.setdefault(user_input, []).append(d_amount)
        return (user_input, donor_dict.get(user_input))
    else:
        try:
            d_amount = int(d_amount)
        except ValueError as error:
            return (type(error).__name__)
        donor_dict.setdefault(user_input, []).append(d_amount)
        return (user_input, donor_dict.get(user_input))


def write_letter():
    for donor in donor_dict.keys():
        with open('/Users/Mandava/Documents/python/IntroPython2016/students/smandava/session6/thankyouletter_{}.txt'.format(donor), 'w') as thankyou_file:
            thankyou_note = ('''Dear {donor}, \n \n Thank you very much for your generous donation of ${amount}.
                                \n \n Regards, \n Seattle Charity Org \n'''
                             .format(donor=donor, amount=donor_dict[donor]))
            thankyou_file.write(thankyou_note)
    return ("Created Thank you letter!")

msg = """
What would you like to do?
To send a thank you: type "s"
To print a report: type "p"
To write a thank you letter to disk: type "w"
To exit: type "x"
"""


def main():
    """Run the main interactive loop."""
    response = ''
    select = {'p': print_report, 's': send_thanks, 'w': write_letter,
              'x': 'break'}
    # keep asking until the users responds with an 'x'
    while True:
        print(msg)
        response = input("==> ").strip()  # strip()in case there are any spaces
        if response == 'p':
            select['p']()
        elif response == 's':
            select['s']()
        elif response == 'w':
            select['w']()
        elif response == 'x':
            break
        else:
            print('please type "s", "p", or "x"')

if __name__ == "__main__":
    main()
