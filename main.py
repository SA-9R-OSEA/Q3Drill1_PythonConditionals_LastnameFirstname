from pyscript import document 

def compute_average(event):
    # Get the input values and convert to float
    math = float(document.getElementById("math").value)
    english = float(document.getElementById("english").value)
    science = float(document.getElementById("science").value)
    socialstudies = float(document.getElementById("socialstudies").value)
    ict = float(document.getElementById("ict").value)


    # Compute average
    average = (math + english + science + socialstudies + ict) / 5

    # Determine pass/fail
    if average >= 75:
        result = "Yes"
    else:
        result = "No"

    # Display results
    document.getElementById("average").innerText = str(round(average, 5))
    document.getElementById("result").innerText = result
