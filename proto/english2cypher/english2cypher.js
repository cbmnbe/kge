function englishParser(searchTextBoxId, codeMirrorEditor){
	const parser = new nearley.Parser(nearley.Grammar.fromCompiled(grammar));
	var text = document.getElementById(searchTextBoxId).value;
	parser.feed(text);
	var text = document.getElementById(searchTextBoxId).value;
	var code = "";
	var result = parser.results[0][0][0][0];
if(result.statementNo==1){
		code += 'MATCH (a:Person)-[:WORKS]-(b:Company)\n\
WHERE a.name = "'+result.english2cypher1personName[0].join("")+'"\n\
RETURN a\n\
';
}

if(result.statementNo==2){
		code += 'MATCH (a:Person)-[:WORKS]-(b:Company)\n\
WHERE b.name = "'+result.english2cypher2companyName[0].join("")+'"\n\
RETURN a\n\
';
}

if(result.statementNo==3){
		code += 'MATCH (a:Person)\n\
RETURN distinct a.name LIMIT '+result.english2cypher3number[0].join("")+'\n\
';
}

if(result.statementNo==4){
		code += 'MATCH (b:Company)\n\
RETURN distinct b.name\n\
';
}

	codeMirrorEditor.setValue(code);
};