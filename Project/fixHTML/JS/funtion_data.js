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
  
    question_cnt = (number - count) % 2
  
    var existingEntries = JSON.parse(localStorage.getItem("allEntries"));
    if(existingEntries == null) existingEntries = [];

    //Radio 버튼 값 불러오기
    var survayValue1 = document.getElementsByName("survay1");
    var survayValue2 = document.getElementsByName("survay2");
    var survayValue3 = document.getElementsByName("survay3");
    if (question_cnt == 0 ){
        var survayValue4 = document.getElementsByName("survay4");
    }
    // 두 개의 값이 체크되어 있는지 검사
    var chk_cnt = 0;

    for(var i=0; i<survayValue1.length; i++){
        if(survayValue1[i].checked==true){
            chk_cnt++;
        }
        if(survayValue2[i].checked==true){
            chk_cnt++;
        }
        if(survayValue3[i].checked==true){
            chk_cnt++;
        }
        if (question_cnt == 0 ){
            if(survayValue4[i].checked==true){
                chk_cnt++;
            }
        }
    }

    // 두 가지 항목이 체크되어 있지 않으면 알람 후 재입력 유도
    if ( question_cnt != 0 ){
        if(chk_cnt<3){
            alert('체크하세요');
            return;
        }
    }
    else{
        if(chk_cnt<4){
            alert('체크하세요');
            return;
        }
    }

    
    //라디오 버튼이 체크되었나 확인하기 위한 변수
    for(var i = 0; i<survayValue1.length; i++){
        //만약 라디오 버튼이 체크가 되어있다면 true
        if(survayValue1[i].checked==true){
            //버튼 값 알림 후 value push
            alert(survayValue1[i].value);
            existingEntries.push(survayValue1[i].value);
        }
       
    }
    for(var i = 0; i<survayValue2.length; i++){
        if(survayValue2[i].checked==true){
            //버튼 값 알림 후 value push
            alert(survayValue2[i].value);
            existingEntries.push(survayValue2[i].value);
        }
    }

    for(var i = 0; i<survayValue3.length; i++){
        if(survayValue3[i].checked==true){
            alert(survayValue3[i].value);
            existingEntries.push(survayValue3[i].value);
        }
    }
    if ( question_cnt == 0){
        for(var i = 0; i<survayValue4.length; i++){
            if(survayValue4[i].checked==true){
                alert(survayValue4[i].value);
                existingEntries.push(survayValue4[i].value);
            }
        }
    }

    //값 저장 후 페이지 이동
    localStorage.setItem("allEntries", JSON.stringify(existingEntries));
    location.href = "http://127.0.0.1:5500/Project/fixHTML/html/"+number+'~'+".html?"+number;
};

/*이전 페이지로 이동*/
function previous_Page(tid, question_cnt, number){
    // Session에 저장되어 있느 배열 불러오기
    var existingEntries = JSON.parse(localStorage.getItem("allEntries"));

    //이전을 누르면 기존에 저장된 2개 value 삭제
  
    if(question_cnt % 2 != 0){
    existingEntries.pop();
    existingEntries.pop();
    existingEntries.pop();
    }

    else{
    existingEntries.pop();
    existingEntries.pop();
    existingEntries.pop();
    existingEntries.pop();
    }
    

    //값 저장 후 페이지 이동
    localStorage.setItem("allEntries", JSON.stringify(existingEntries));
    location.href = "http://127.0.0.1:5500/htmlProject/fixHTML/html/"+number+'~'+".html?"+number;
}

// 이전 페이지 -> 메인 페이지
function main_page(){
    location.href = "http://127.0.0.1:5500/Project/fixHTML/html/main.html";
}

// 저장된 데이터 JSP에 전달
$(function dataSend(){
    var gt = localStorage.getItem("allEntries");
    document.getElementById("checkData").value = gt;
    return gt;
 });

// 저장된 세션 삭제
function clearSesstion(){
    localStorage.clear();
    
}