import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    print(df)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()
    print(race_count)

    # What is the average age of men?

    male_only_df = df[df["sex"] == "Male"]
    average_age_men = male_only_df["age"].mean().round(1)
    print(average_age_men)
    

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df["education"].value_counts(normalize=True).mul(100).round(1).loc["Bachelors"]
    print(percentage_bachelors)
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    high_ed_list = ["Bachelors", "Masters", "Doctorate"]
    filtered_higher_ed_count = df[df["education"].isin(high_ed_list)].shape[0]
    filtered_higher_ed_more_50k = df[(df["education"].isin(high_ed_list)) & (df["salary"] == ">50K")].shape[0]
    higher_education_rich = round((filtered_higher_ed_more_50k/filtered_higher_ed_count)*(100), 1)

    filtered_lower_ed_count = df[~df["education"].isin(high_ed_list)].shape[0]
    print(filtered_higher_ed_count)
    filtered_lower_ed_more_50k = df[(~df["education"].isin(high_ed_list)) & (df["salary"] == ">50K")].shape[0]
    print(filtered_higher_ed_more_50k)
    lower_education_rich = round((filtered_lower_ed_more_50k/filtered_lower_ed_count)*(100), 1)

    # percentage with salary >50K


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].unique().min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    num_min_workers = df[df["hours-per-week"] == min_work_hours].shape[0]
    print(num_min_workers)

    rich_percentage = round((df[(df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")].shape[0]/num_min_workers)*100, 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country_num = df["native-country"].value_counts()
    highest_earning_country_50k = df[df["salary"] == ">50K"]["native-country"].value_counts()
    highest_earning_country_percentages_list = (highest_earning_country_50k/highest_earning_country_num).mul(100).round(1)



    highest_earning_country = highest_earning_country_percentages_list.idxmax()
    highest_earning_country_percentage = highest_earning_country_percentages_list.max()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[df["native-country"] == "India"]["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
