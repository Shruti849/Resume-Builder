window.onload = function () {
    document.getElementById("download")
        .addEventListener("click", () => {
            const template1 = this.document.getElementById("template1");
            console.log(template1);
            console.log(window);
           // html2pdf().from(invoice1).save();
            var opt = {
                filename: 'My Resume.pdf',
                margin:-1,
                image:{type:'pdf',quality:0.98},
                html2canvas:{scale:1},
                jsPDF:{unit:'in',format:'letter'}
                
            };
            html2pdf().from(template1).set(opt).save();
        })

    document.getElementById("download1")
        .addEventListener("click", () => {
            const template2 = this.document.getElementById("template2");
            console.log(template2);
            console.log(window);
            // html2pdf().from(invoice).save();
            var opt = {
                filename: 'My Resume.pdf',
                margin:0,
                image:{type:'pdf',quality:0.98},
                html2canvas:{scale:1},
                jsPDF:{unit:'in',format:'letter'}

            };
            html2pdf().from(template2).set(opt).save();
        })



    document.getElementById("download2")
        .addEventListener("click", () => {
            const template3 = this.document.getElementById("template3");
             console.log(template3);
            console.log(window);
            // html2pdf().from(invoice).save();
            var opt = {
            filename: 'My Resume.pdf',
            margin:0,
            image:{type:'pdf',quality:0.98},
            html2canvas:{scale:1},
            jsPDF:{unit:'in',format:'letter'}

        };
        html2pdf().from(template3).set(opt).save();
        })

    document.getElementById("download3")
        .addEventListener("click", () => {
            const template4 = this.document.getElementById("template4");
            console.log(template4);
            console.log(window);
            // html2pdf().from(invoice).save();
            var opt = {
                filename: 'My Resume.pdf',
                margin:-0.5,
                image:{type:'pdf',quality:0.98},
                html2canvas:{scale:1},
                jsPDF:{unit:'in',format:'letter'}

            };
            html2pdf().from(template4).set(opt).save();
        })
        
    document.getElementById("download4")
    .addEventListener("click", () => {
        const template5 = this.document.getElementById("template5");
        console.log(template5);
        console.log(window);
        // html2pdf().from(invoice).save();
        var opt = {
            filename: 'My Resume.pdf',
            margin:-0.5,
            image:{type:'pdf',quality:0.98},
            html2canvas:{scale:1},
            jsPDF:{unit:'in',format:'letter'}

        };
        html2pdf().from(template5).set(opt).save();
    })


}