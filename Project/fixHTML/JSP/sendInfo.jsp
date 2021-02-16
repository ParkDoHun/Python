<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="UTF-8"%>
<%@ page import = "dbConn.connectServer" %>


<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>send_result_Page</title>
</head>
<body>
	<%
		request.setCharacterEncoding("utf-8");
		connectServer connect = connectServer.getInstance();
		String SNAME = request.getParameter("SNAME");
		String UGRADE = request.getParameter("UGRADE");
		String UCLASS = request.getParameter("UCLASS");
		String UNUMBER = request.getParameter("UNUMBER");
		String UNAME = request.getParameter("UNAME");
		String USEX = request.getParameter("USEX");
		String UEMAIL = request.getParameter("email_id") + "@" + request.getParameter("email");
		String UMNUMBER = request.getParameter("txtMobile1") + request.getParameter("txtMobile2") + request.getParameter("txtMobile3");
		String AGREEMENT = request.getParameter("AGREEMENT");
		String TID = request.getParameter("TID");

		out.println(SNAME);
		out.println(UGRADE);
		out.println(UCLASS);
		out.println(UNUMBER);
		out.println(UNAME);
		out.println(USEX);
		out.println(UEMAIL);
		out.println(UMNUMBER);
		out.println(AGREEMENT);
		out.println(TID);
		
		System.out.println(connect.sendInfo(SNAME, UGRADE, UCLASS, UNUMBER, UNAME, USEX, UEMAIL, UMNUMBER, AGREEMENT));
		
		pageContext.forward("../"+TID+"/1.html");
		
	%>

</body>
</html>