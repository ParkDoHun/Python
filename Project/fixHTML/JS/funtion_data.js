

/*split을 이용하여 url에서 number 추출*/
function splitNumber(){
    var arSplitUrl = location.href.split('?');
    questionNumber = Number(arSplitUrl[1]);
    return questionNumber;
}
/*split을 이용하여 url에서 page 추출 */
function splitPage(){
    var arSplitUrl = location.href.split("/");    
    var nArLength = arSplitUrl.length;
    var arFileName = arSplitUrl[nArLength-1]; 
    var arSplitFileName = arFileName.split("~.");
    var sFileName = arSplitFileName[0];
    return Number(sFileName);

    
} 

/*다음 페이지로 이동과 동시에 Session에 값 추가*/
function next_Page(tid, count, number) {
  
    question_cnt = number - count
  
    var existingEntries = JSON.parse(localStorage.getItem("allEntries"));
    if(existingEntries == null) existingEntries = [];

    //Radio 버튼 값 불러오기
    var survayValue1 = document.getElementsByName("survay1");
    var survayValue2 = document.getElementsByName("survay2");
   
    if (question_cnt >= 3){
        var survayValue3 = document.getElementsByName("survay3");
    }

    if (question_cnt >= 4 ){
        var survayValue4 = document.getElementsByName("survay4");
    }
    

   
    // 두 개의 값이 체크되어 있는지 검사
    var chk_cnt = 0;

    for(var i=0; i<survayValue1.length; i++){
        if(survayValue1[i].checked==true){
            chk_cnt++;
        }
    }
    for( i = 0; i<survayValue2.length; i++){
        if(survayValue2[i].checked==true){
            chk_cnt++;
            }
        }
        if (question_cnt >= 3){
            for(i = 0; i<survayValue3.length; i++){
        if(survayValue3[i].checked==true){
            chk_cnt++;
            }
        }
    }
        if (question_cnt >= 4 ){
            for( i = 0; i<survayValue4.length; i++) {
            if(survayValue4[i].checked==true){
                chk_cnt++;
                 }
            }
        }
     

    // 두 가지 항목이 체크되어 있지 않으면 알람 후 재입력 유도

    if(question_cnt == 2){
        if(chk_cnt<2){
            alert('체크되지 않은 문항이 있습니다');
            return;
        }
    }

    else if ( question_cnt == 3 ){
        if(chk_cnt<3){
            alert('체크되지 않은 문항이 있습니다');
            return;
        }
    }
    else{
        if(chk_cnt<4){
            alert('체크되지 않은 문항이 있습니다');
            return;
        }
    }

    
    //라디오 버튼이 체크되었나 확인하기 위한 변수
    for(var i = 0; i<survayValue1.length; i++){
        //만약 라디오 버튼이 체크가 되어있다면 true
        if(survayValue1[i].checked==true){
            //버튼 값 알림 후 value push
            existingEntries.push(survayValue1[i].value);
        }
       
    }
    for(var i = 0; i<survayValue2.length; i++){
        if(survayValue2[i].checked==true){
            //버튼 값 알림 후 value push
            existingEntries.push(survayValue2[i].value);
        }
    }
    if (question_cnt == 3){
    for(var i = 0; i<survayValue3.length; i++){
        if(survayValue3[i].checked==true){
            existingEntries.push(survayValue3[i].value);
        }
    }
}
    if ( question_cnt == 4){
        for(var i = 0; i<survayValue4.length; i++){
            if(survayValue4[i].checked==true){
                existingEntries.push(survayValue4[i].value);
            }
        }
    }


    

    //값 저장 후 페이지 이동
    localStorage.setItem("allEntries", JSON.stringify(existingEntries));

    if(number == 187){
        endSurvay();
    }
    else{
        location.href = "http://127.0.0.1:5500/fixHTML/"+tid+'/'+number+'~'+".html?"+number;
    }
};

/*이전 페이지로 이동*/
function previous_Page(tid, question_cnt, number){
    // Session에 저장되어 있느 배열 불러오기
    var existingEntries = JSON.parse(localStorage.getItem("allEntries"));

    //이전을 누르면 기존에 저장된 2개 value 삭제

    for(i=0; i<question_cnt; i++){
        existingEntries.pop();
    }
    

    //값 저장 후 페이지 이동
    localStorage.setItem("allEntries", JSON.stringify(existingEntries));
    location.href = "http://127.0.0.1:5500/fixHTML/"+tid+'/'+number+'~'+".html?"+number;
}
// 저장된 세션 삭제


function endSurvay(){
    location.href = "http://127.0.0.1:5500/fixHTML/end.html";
}
