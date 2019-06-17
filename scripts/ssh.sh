#!/usr/bin/env bash
function person()
{   
	pessoa=$f_1
	ssh -i ~/.ssh/id_rsa user@server "multichain-cli chain_bio liststreamkeyitems stream_bio "${pessoa}" | jq '.[0] .data .json'" > $pessoa
}

while getopts f: OPCAO;
do
	case "${OPCAO}" in
		f) f_1="${OPTARG}" ;;
	esac
done

[ ${f_1} ] && person