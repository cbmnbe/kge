main -> (statement):+
statement -> string11 english2cypher1personName string12 {%
	function(data) {
		return {
			statementNo: 1,
			english2cypher1personName: data[1]
		};
	}
%}
string11 -> [Cc] [Oo] [Mm] [Pp] [Aa] [Nn] [Ii] [Ee] [Ss] [ ] [Tt] [Hh] [Aa] [Tt] [ ] [Pp] [Ee] [Rr] [Ss] [Oo] [Nn] [ ] 
string12 -> [ ] [Ii] [Ss] [ ] [Ww] [Oo] [Rr] [Kk] [Ii] [Nn] [Gg] [ ] [Ww] [Ii] [Tt] [Hh] 
english2cypher1personName -> [a-zA-Z0-9 -.,]:+

statement -> string21 english2cypher2companyName {%
	function(data) {
		return {
			statementNo: 2,
			english2cypher2companyName: data[1]
		};
	}
%}
string21 -> [Aa] [Ll] [Ll] [ ] [Tt] [Hh] [Ee] [ ] [Pp] [Ee] [Oo] [Pp] [Ll] [Ee] [ ] [Ww] [Oo] [Rr] [Kk] [Ii] [Nn] [Gg] [ ] [Ff] [Oo] [Rr] [ ] [Tt] [Hh] [Ee] [ ] [Cc] [Oo] [Mm] [Pp] [Aa] [Nn] [Yy] [ ] 
english2cypher2companyName -> [a-zA-Z0-9 -.,]:+

statement -> string31 english2cypher3number {%
	function(data) {
		return {
			statementNo: 3,
			english2cypher3number: data[1]
		};
	}
%}
string31 -> [Aa] [Ll] [Ll] [ ] [Tt] [Hh] [Ee] [ ] [Pp] [Ee] [Oo] [Pp] [Ll] [Ee] [ ] [Ii] [Nn] [ ] [Tt] [Hh] [Ee] [ ] [Dd] [Aa] [Tt] [Aa] [Bb] [Aa] [Ss] [Ee] [ ] [Ll] [Ii] [Mm] [Ii] [Tt] [ ] [Tt] [Oo] [ ] 
english2cypher3number -> [0-9]:+

statement -> string41 {%
	function(data) {
		return {
			statementNo: 4,
		};
	}
%}
string41 -> [Aa] [Ll] [Ll] [ ] [Tt] [Hh] [Ee] [ ] [Cc] [Oo] [Mm] [Pp] [Aa] [Nn] [Ii] [Ee] [Ss] [ ] [Ii] [Nn] [ ] [Tt] [Hh] [Ee] [ ] [Dd] [Aa] [Tt] [Aa] [Bb] [Aa] [Ss] [Ee] 

