const rangeSliderAmount = document.getElementById('range-slider-amount')
const min_price = parseInt(document.getElementById('min_amount').value)
const max_price = parseInt(document.getElementById('max_amount').value)

const min = parseInt(document.getElementById('id_min_insurance_amount').value)
const max = parseInt(document.getElementById('id_max_insurance_amount').value)


if (rangeSliderAmount) {
    if (isNaN(min) || isNaN(max)) {
        noUiSlider.create(rangeSliderAmount, {
            start: [min_price, max_price],
            connect: true,
            step: 1,
            range: {
                'min': [min_price],
                'max': [max_price]
            }
        });
    } else {
        noUiSlider.create(rangeSliderAmount, {
            start: [min, max],
            connect: true,
            step: 1,
            range: {
                'min': [min_price],
                'max': [max_price]
            }
        });
    }


    const input0 = document.getElementById('id_min_insurance_amount')
    const input1 = document.getElementById('id_max_insurance_amount')
    const inputs = [input0, input1]

    const rangeinput0 = document.getElementById('range-amount-0');
    const rangeinput1 = document.getElementById('range-amount-1');
    const rangeinputs = [rangeinput0, rangeinput1];

    rangeSliderAmount.noUiSlider.on('update', function (values, handle) {
        rangeinputs[handle].value = Math.round(values[handle]);
        inputs[handle].value = Math.round(values[handle]);
    })


    const setRangeSlider = (i, value) => {
        let arr = [null, null];
        arr[i] = value;
        rangeSliderAmount.noUiSlider.set(arr)
    };

    rangeinputs.forEach((el, index) => {
        el.addEventListener('change', (e) => {
            setRangeSlider(index, e.currentTarget.value);
        });
    });

}
