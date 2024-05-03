import tkinter

window = tkinter.Tk()
window.title("Loan Calculator")

annual_interest_label = tkinter.Label(text="Annual Loan Rate")
annual_interest_label.grid(row=1, column=0)

annual_interest_input = tkinter.Entry(width=10)
annual_interest_input.grid(row=1, column=2)

year_label = tkinter.Label(text="Number of Years")
year_label.grid(row=3, column=0)

year_input = tkinter.Entry()
year_input.grid(row=3, column=2)

loan_amount_label = tkinter.Label(text="Loan Amount")
loan_amount_label.grid(row=5, column=0)

loan_amount_input = tkinter.Entry()
loan_amount_input.grid(row=5, column=2)

mon_pay_label_1 = tkinter.Label(text="Monthly Payment")
mon_pay_label_1.grid(row=7, column=0)

mon_pay_label_2 = tkinter.Label(font=("Arial", 10, "bold"))
mon_pay_label_2.grid(row=7, column=2)

tot_pay_label_1 = tkinter.Label(text="Total Payment")
tot_pay_label_1.grid(row=9, column=0)

tot_pay_label_2 = tkinter.Label(font=("Arial", 10, "bold"))
tot_pay_label_2.grid(row=9, column=2)


def compute_payment():
    annual_interest = annual_interest_input.get()
    year = year_input.get()
    loan = loan_amount_input.get()
    for i in range(int(year)):
        tot_pay_label_2.config(text=round(float(loan) + float(loan) * (float(annual_interest) / 100), 2))
        mon_pay_label_2.config(
            text=round((float(loan) + float(loan) * (float(annual_interest) / 100)) / (float(year) * 12), 2))


calculate_button = tkinter.Button(text="Compute Payment", command=compute_payment)
calculate_button.grid(row=11, column=1)

window.mainloop()