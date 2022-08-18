from decimal import Decimal, ROUND_HALF_UP

def main():

    # Sample marks in each CA component
    labs = 60
    bucket_list = 100
    labexam_01 = 47
    labexam_02 = 68

    ca = (1 * labs) + (2 * bucket_list) + (3 * labexam_01) + (4 * labexam_02)
    ca = ca / 10

    # Round to nearest integer (with .5 always rounding up)
    ca = int(Decimal(ca).to_integral_value(ROUND_HALF_UP))

    print(f'Your overall CA mark is: {ca:d}%')

if __name__ == "__main__":
    main()