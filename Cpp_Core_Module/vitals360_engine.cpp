#include <iostream>
#include <string>
using namespace std;

float calculateBMI(float weight, float height) {
    return weight / (height * height);
}

int calculateCalories(int steps, int activeMinutes, int exerciseMinutes) {
    return (steps * 0.04) + (activeMinutes * 4) + (exerciseMinutes * 6);
}

int calculateActivityScore(int steps, int activeMinutes, int exerciseMinutes) {
    return (steps / 100) + (activeMinutes * 2) + (exerciseMinutes * 3);
}

bool postureAlert(int postureScore) {
    return postureScore < 60;
}

string fitnessBadge(int activityScore) {
    if (activityScore >= 200)
        return "🏆 Champion Badge";
    else if (activityScore >= 150)
        return "🥇 Gold Badge";
    else if (activityScore >= 100)
        return "🥈 Silver Badge";
    else if (activityScore >= 50)
        return "🥉 Bronze Badge";
    else
        return "No Badge";
}

void stepSummary(int dailySteps) {
    cout << "\nStep Summary:\n";
    cout << "Daily Steps: " << dailySteps << endl;
    cout << "Weekly Steps: " << dailySteps * 7 << endl;
    cout << "Monthly Steps: " << dailySteps * 30 << endl;
    cout << "Yearly Steps: " << dailySteps * 365 << endl;
}


int main() {
    int dailySteps, activeMinutes, exerciseMinutes, postureScore;
    float weight, height;
    char choice;

    cout << "===== Vitals360 Fitness Tracking Engine =====\n\n";

    do {
        cout << "Enter weight (kg): ";
        cin >> weight;

        cout << "Enter height (meters): ";
        cin >> height;

        cout << "Enter daily steps: ";
        cin >> dailySteps;

        cout << "Enter active minutes: ";
        cin >> activeMinutes;

        cout << "Enter exercise time (minutes): ";
        cin >> exerciseMinutes;

        cout << "Enter posture score (0-100): ";
        cin >> postureScore;

        if (weight <= 0 || height <= 0 || dailySteps < 0 ||
            activeMinutes < 0 || exerciseMinutes < 0 ||
            postureScore < 0 || postureScore > 100) {
            cout << "\nInvalid input detected. Try again.\n\n";
            continue;
        }

        float bmi = calculateBMI(weight, height);
        int calories = calculateCalories(dailySteps, activeMinutes, exerciseMinutes);
        int activityScore = calculateActivityScore(dailySteps, activeMinutes, exerciseMinutes);
        bool postureWarning = postureAlert(postureScore);
        string badge = fitnessBadge(activityScore);

        cout << "\n----- FITNESS SUMMARY -----\n";
        cout << "BMI: " << bmi << endl;
        cout << "Calories Burned: " << calories << " kcal\n";
        cout << "Activity Score: " << activityScore << endl;

        stepSummary(dailySteps);

        if (postureWarning)
            cout << "Posture Alert: ⚠ Poor posture detected!\n";
        else
            cout << "Posture Status: ✅ Good posture maintained\n";

        cout << "Badge Earned: " << badge << endl;
        cout << "----------------------------\n\n";

        cout << "Enter another record? (y/n): ";
        cin >> choice;
        cout << endl;

    } while (choice == 'y' || choice == 'Y');

    cout << "Vitals360 system closed successfully.\n";
    return 0;
}



