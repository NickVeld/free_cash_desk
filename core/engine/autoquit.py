def autoquit_run(tapi):
    for user in tapi.get_ready_for_autoquit():
        pers_id = int(user['pers_id'])
        for worker in tapi.workers_list:
            worker.quit(pers_id, pers_id, "Вы были неактивны долгое время.\n")

#TODO: It can be needed to finish.