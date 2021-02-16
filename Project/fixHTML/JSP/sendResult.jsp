<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%@ page import = "dbConn.connectServer" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>send_result_Page</title>

<!-- js 파일 include -->
<script type="text/javascript" src="./JSP/funtion_data.js">
	var getData = dataSend();
</script> 
</head>
<body>

	<%
		getData;
		connectServer connect = connectServer.getInstance();
		//int[] result = request.getParameterValues("survay2");
		//String UID = request.getParameter("UID");
		//String TID = request.getParameter("TID");
		//String TESTDATE = request.getParameter("TESTDATE");
		
		int[] result = {3,1,2,3,4,1,3,2,4,5,2,2,5,1,3};
		String UID = "12";
		String TID = "0";
		String TESTDATE = "2021-02-08 06:47:23";
		
		System.out.println(connect.sendTestResult(result, UID, TID, TESTDATE));
		//System.out.println(result[2]);

	%>

</body>
</html>