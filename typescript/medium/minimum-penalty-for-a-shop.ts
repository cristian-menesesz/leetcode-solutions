function bestClosingTime(customers: string): number {
    let penalty = 0;

    for (const c of customers) {
        if (c === "Y") penalty++;
    }

    let minPenalty = penalty;
    let bestHour = 0;

    for (let i = 0; i < customers.length; i++) {
        const c = customers[i];

        if (c === "Y") {
            penalty -= 1;
        } else {
            penalty += 1;
        }

        if (penalty < minPenalty) {
            minPenalty = penalty;
            bestHour = i + 1;
        }
    }

    return bestHour;
}
