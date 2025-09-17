import webbrowser
import os

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smartsheet Order Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            height: 100vh;
        }

        /* Left Column with Ascension Health branding */
        .left-column {
            width: 30%;
            background: linear-gradient(135deg, #005EB8 0%, #0071CE 100%);
            color: #ffffff;
            padding: 20px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: left;
            position: relative;
            overflow-y: auto;
        }
        .left-column::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            background: repeating-linear-gradient(
                45deg,
                rgba(255,255,255,0.05),
                rgba(255,255,255,0.05) 10px,
                transparent 10px,
                transparent 20px
            );
            pointer-events: none;
        }
        .left-column h2 {
            color: white;
            margin-bottom: 20px;
        }
        .left-column .message {
            font-size: 14px;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        .left-column .message a {
            color: white;
            text-decoration: underline;
        }
        .left-column .logo {
            width: 150px;
            margin-top: 20px;
        }

        /* Right Column - Form Area */
        .right-column {
            width: 70%;
            padding: 30px;
            box-sizing: border-box;
            overflow-y: auto;
            background-color: #f9f9f9;
        }

        /* Form Styling */
        form {
            max-width: 700px;
            margin: 0 auto;
        }

        /* Card-like form groups */
        .form-group {
            margin-bottom: 20px;
            padding: 15px 20px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        }
        .form-group h4 {
            margin-top: 0;
            color: #005EB8;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        <h2>Downtime Ordering Form</h2>
        <p class="message">
            In the event that PeopleSoft is not available, this form should be used to request ordering for items that should be processed to a Purchase Order.<br><br>
            If you are ordering more than five items from a Supplier, an Upload Template can be found <strong>HERE</strong>. Please upload completed sheet as an attachment in the Downtime Ordering Form.<br><br>
            If you are placing a MEDLINE order please download form <strong>HERE</strong> and email it to: <a href="mailto:purchasingforms@ascension.org">purchasingforms@ascension.org</a>.<br><br>
            For Health Ministry location/GL information, item ordering information, or supplier account information, please see <strong>Downtime Toolkit</strong>.<br><br>
            If you have questions regarding this form, please click the <strong>Requester Support Site</strong> link or call at 1-833-277-8724.
        </p>
        <img src="ascension-logo.png" alt="Ascension Health Logo" class="logo">
            <div class="form-group" id="health_ministry_codes_container" style="display:none;">
                <label for="health_ministry_codes">Health Ministry Codes</label>
                <select id="health_ministry_codes" name="health_ministry_codes"></select>
            <div class="form-group">
                <label for="order_lines_total">How many order lines do you need?</label>
                <select id="order_lines_total" name="order_lines_total" required>
                    <option value="" disabled selected>Select number of lines</option>
                    <!-- 1-20 options -->
                    ${[...Array(20)].map((_,i) => `<option value="${i+1}">${i+1}</option>`).join('')}
            header.innerHTML = `Item ${i} <span style="font-size: 14px;">&#9660;</span>`;
            const content = document.createElement('div');
            content.style.display = 'none';
            content.style.marginTop = '10px';

            content.innerHTML = `
                <label for="item_${i}_id">Item ID (PS #)</label>
                <input type="text" id="item_${i}_id" name="item_${i}_id">
                <label for="item_${i}_supplier_id">Supplier Item ID</label>
                <input type="text" id="item_${i}_supplier_id" name="item_${i}_supplier_id">
                <label for="item_${i}_in_unit">IN UNIT</label>
                <input type="text" id="item_${i}_in_unit" name="item_${i}_in_unit">
                <label for="item_${i}_serial_lot">Serial/Lot #</label>
                <input type="text" id="item_${i}_serial_lot" name="item_${i}_serial_lot">
                <label for="item_${i}_description">Item Description</label>
                <input type="text" id="item_${i}_description" name="item_${i}_description">
                <label for="item_${i}_uom">UOM</label>
                <input type="text" id="item_${i}_uom" name="item_${i}_uom">
                <label for="item_${i}_qty">QTY</label>
                <input type="number" id="item_${i}_qty" name="item_${i}_qty">
                <label for="item_${i}_price">PRICE</label>
                <input type="number" id="item_${i}_price" name="item_${i}_price">
            `;

            header.addEventListener('click', () => {
                if(content.style.display==='none'){
                    content.style.display='block';
                    header.querySelector('span').innerHTML='&#9650;';
                } else {
                    content.style.display='none';
                    header.querySelector('span').innerHTML='&#9660;';
                }
            });

            div.appendChild(header);
            div.appendChild(content);
            dynamicContainer.appendChild(div);
        }
    });

    // Health Ministry Code Logic
    const healthMinistry = document.getElementById('health_ministry');
    const codesContainer = document.getElementById('health_ministry_codes_container');
    const codesSelect = document.getElementById('health_ministry_codes');

    const ministryCodes = {
        "ALBIR":["C0504","P0004","50531","50532","50535","50541","50542"],
        "CTBRI":["48514"],
        "DCWAS":["P0006","C0006","24005"],
        "FLJAC":["P0008","52005","C0008","52012","52009","52015"],
        "FLPEN":["26012","P0001","C0001","26013","26016","26042"],
        "ILARL":["C0035","66004","P0035","66008","66510","66511","66512","66513","66514","66520","66521","66522","66523","66201"],
        "INEVA":["C0010","40011","P0010","40017","40030"],
        "ININD":["P0011","46006","46013","46014","46018","C0011","46019","46024","46029","46033","46036","46042","46045","46046","46047","46048","46049","46055","46091"],
        "KSWIC":["P0032","C0032","68012","68076","68013","68022","68023"],
        "MDBAL":["C0012","32018","32022"],
        "MIDET":["C0013","P0013","34014","34015","34017","34023","34030","34031"],
        "MIGRA":["C0014","P0014","12018"],
        "MIKAL":["C0015","54005","P0015","54009","54020"],
        "MIROC":["73000","C0049","C0050"],
        "MISAG":["44005","44006","C0016"],
        "MITAW":["36003"],
        "MOSTL":["P0019","A0010","62003","62088","C0019"],
        "OKTUL":["C0033","P0033","72007","72010","72011","72012","72017","72029","72049"],
        "TNNAS":["P0003","C0003","28008","28012","28022","28029","28039","28040","28041","28042","28059"],
        "TXAUS":["30002","P0024","30003","C0024","30014","30017","30019","30020","30024","30049","30055","30061","30074","30078","30079"],
        "TXWAC":["20001","C0025","P0025","20002"],
        "WIAPP":["C0034","P0034","71139","71140","71142"],
        "WIMIL":["60005","C0027","P0027","60008","60017","74000","C0037","C0045","P0045","74002","P0039","C0039","P0043","74003","C0047","74004","C0044","P0044","P0037","74009","C0046","74010","74011","P0042","C0042","P0038","74027","C0041","74034"]
    };

    healthMinistry.addEventListener('change', () => {
        const selected = healthMinistry.value;
        codesSelect.innerHTML = '';
        if(selected && ministryCodes[selected]){
            ministryCodes[selected].forEach(code=>{
                const opt = document.create
# Save HTML file
file_name = "form_preview.html"
with open(file_name, "w", encoding="utf-8") as f:
    f.write(html_content)

# Open in default web browser
file_path = os.path.abspath(file_name)
webbrowser.open(f"file://{file_path}")