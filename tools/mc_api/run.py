from mailchimp3 import MailChimp
import yaml
import datetime
import operator

with open("credentials.yaml", "r") as infile:
  try:
    mc_yaml = yaml.load(infile)
  except:
    print "Couldn't load credentials. Exiting"
    exit()

client = MailChimp(mc_api=mc_yaml["mc_api"], mc_user=mc_yaml["mc_user"])
# campaign_data = []
today = datetime.date.today()
margin = datetime.timedelta(days=7)
campaigns = client.campaigns.all(get_all=True)
for campaign in campaigns["campaigns"]:
  try:
    if today - margin <= datetime.datetime.strptime(campaign["send_time"][:10], "%Y-%m-%d").date() <= today:
      last_campaign = campaign
      # campaign_data.append([campaign["send_time"][:10], str(campaign["id"]), str(campaign['emails_sent']), campaign["recipients"]["list_name"], str(campaign["settings"]["subject_line"]), str(
      #   int(campaign['report_summary']["open_rate"]*100)) + "%", str(int(campaign['report_summary']["click_rate"]*100)) + "%",  campaign["archive_url"]])
      break
  except:
    print "Looks like no campaign date or another issue"


clicks = client.reports.click_details.all(campaign_id=last_campaign["id"], count=100)
click_dict = {}
for link in clicks["urls_clicked"]:
  if link["url"] in click_dict:
    continue
  click_dict[link["url"]] = link["unique_click_percentage"]

sorted_x = sorted(click_dict.items(), key=operator.itemgetter(1))

print "The most clicked last week was [THIS]({0}) with {1:.1f}% opens.".format(sorted_x[-1][0], sorted_x[-1][1]*100)
