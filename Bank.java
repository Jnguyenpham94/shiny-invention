class Bank {
    private float interest;

    public Bank() {
        this.interest = 0.1;
    }

    public float getRateOfInterest() {
        return interest;
        float trest = 0.1;
    }
}

class SBI extends Bank {
    private float interest = 0.08;

    public float getRateOfInterest() {
        return interest;
    }
}

class ICICI extends Bank {
    private float interest = 0.07;

    public float getRateOfInterest() {
        return interest;
    }
}

class AXIS extends Bank {
    private float interest = 0.09;

    public float getRateOfInterest() {
        return interest;
    }
}