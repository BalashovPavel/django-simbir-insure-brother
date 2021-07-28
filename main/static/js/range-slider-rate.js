const rangeSliderRate = document.getElementById('range-slider-rate')
const min_rate = parseInt(document.getElementById('min_rate').value)
const max_rate = parseInt(document.getElementById('max_rate').value)

const min1 = parseInt(document.getElementById('id_min_interest_rate').value)
const max1 = parseInt(document.getElementById('id_max_interest_rate').value)


if (rangeSliderRate) {
    if (isNaN(min1) || isNaN(max1)) {
        noUiSlider.create(rangeSliderRate, {
            start: [min_rate, max_rate],
            connect: true,
            step: 1,
            range: {
                'min': [min_rate],
                'max': [max_rate]
            }
        });
    } else {
        noUiSlider.create(rangeSliderRate, {
            start: [min1, max1],
            connect: true,
            step: 1,
            range: {
                'min': [min_rate],
                'max': [max_rate]
            }
        });
    }


    const input0 = document.getElementById('id_min_interest_rate')
    const input1 = document.getElementById('id_max_interest_rate')
    const inputs = [input0, input1]

    const rangeinput0 = document.getElementById('range-rate-0');
    const rangeinput1 = document.getElementById('range-rate-1');
    const rangeinputs = [rangeinput0, rangeinput1];

    rangeSliderRate.noUiSlider.on('update', function (values, handle) {
        rangeinputs[handle].value = Math.round(values[handle]);
        inputs[handle].value = Math.round(values[handle]);
    })


    const setRangeSlider = (i, value) => {
        let arr = [null, null];
        arr[i] = value;
        rangeSliderRate.noUiSlider.set(arr)
    };

    rangeinputs.forEach((el, index) => {
        el.addEventListener('change', (e) => {
            setRangeSlider(index, e.currentTarget.value);
        });
    });

}
