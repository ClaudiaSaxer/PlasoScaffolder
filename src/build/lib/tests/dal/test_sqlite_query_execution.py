# -*- coding: utf-8 -*-
"""test class"""
import os
import unittest

from plasoscaffolder.dal import sqlite_query_execution
from tests.test_helper import path_helper


class SQLiteQueryExecutionTest(unittest.TestCase):
  """test the SQLite query execution test"""

  def setUp(self):
    database_path = path_helper.TestDatabasePath()
    file_path = os.path.join(database_path, 'twitter_ios.db')
    self.execute = sqlite_query_execution.SQLQueryExecution(file_path)

  def testRollbackWorks(self):
    """testing if the rollback works"""
    query_select_all_users = 'SELECT * FROM Users'
    query_drop_table = 'DROP TABLE Users'
    result_users_before = self.execute.executeQuery(query_select_all_users)
    result_drop_table = self.execute.executeQuery(query_drop_table)
    result_users_after = self.execute.executeQuery(query_select_all_users)

    self.assertEqual(len(result_users_before.data),
                     len(result_users_after.data))
    self.assertTrue(len(result_users_after.data) is 25)
    self.assertTrue(len(result_users_before.data) is 25)
    self.assertFalse(result_drop_table.has_error)
    self.assertIsNone(result_drop_table.error_message)

  def testMultipleTestAfterOneAnother(self):
    """test two querys after another to test the connection is still open"""
    query_simple = (
      'SELECT createdDate, updatedAt, screenName, name, profileImageUrl,'
      'location, description, url, following, followersCount, '
      'followingCount'
      ' FROM Users ORDER BY createdDate')
    result_simple = self.execute.executeQuery(query_simple)

    query_join = ('SELECT Statuses.date AS date, Statuses.text AS text,'
                  ' Statuses.userId AS user_id, Users.name AS name, '
                  'Statuses.retweetCount AS '
                  'retweetCount, Statuses.favoriteCount AS favoriteCount, '
                  'Statuses.favorited AS favorited, Statuses.updatedAt AS '
                  'updatedAt '
                  'FROM Statuses LEFT join Users ON Statuses.userId = Users.id '
                  'ORDER BY date')
    result_join = self.execute.executeQuery(query_join)

    self.assertIsNone(result_join.error_message)
    self.assertIsNone(result_simple.error_message)
    self.assertFalse(result_simple.has_error)
    self.assertFalse(result_join.has_error)
    self.assertEqual(len(result_join.data), 67)
    self.assertEqual(len(result_simple.data), 25)

  def testQueryErrorNoSuchColumn(self):
    """test two querys after another to test the connection is still open"""
    query = 'SELECT createdDates FROM Users'
    result = self.execute.executeQuery(query)
    expected_error = 'no such column: createdDates'
    self.assertTrue(result.has_error)
    self.assertIsNone(result.data)
    self.assertEqual(str(result.error_message), expected_error)

  def testQueryErrorNoSuchTable(self):
    """test two querys after another to test the connection is still open"""
    query = 'SELECT createdDate FROM Userss'
    result = self.execute.executeQuery(query)
    expected_error = 'no such table: Userss'
    self.assertTrue(result.has_error)
    self.assertIsNone(result.data)
    self.assertEqual(str(result.error_message), expected_error)

  def testExecuteQuerySimple(self):
    """test the execution of a simple query"""
    query = ('SELECT createdDate, updatedAt, screenName, name, profileImageUrl,'
             'location, description, url, following, followersCount, '
             'followingCount'
             ' FROM Users ORDER BY createdDate')
    result = self.execute.executeQuery(query)
    expected_data = [(1177252957.0, 1449070544.333328, 'BBCBreaking',
                      'BBC Breaking News',
                      'https://pbs.twimg.com/profile_images'
                      '/460740982498013184/wIPwMwru_normal.png',
                      'London, UK',
                      'Breaking news alerts and updates from the BBC. For '
                      'news, features, analysis follow @BBCWorld ('
                      'international) or @BBCNews (UK). Latest sport news '
                      '@BBCSport.',
                      'http://www.bbc.co.uk/news', 0, 19466932, 3), (
                       1202704910.0, 1449070777.57104, 'github', 'GitHub',
                       'https://pbs.twimg.com/profile_images/616309728688238592'
                       '/pBeeJQDQ_normal.png',
                       'San Francisco, CA', 'How people build software',
                       'https://t.co/FoKGHcCyJJ', 0, 742086, 172), (
                       1208195714.0, 1449070777.562435, 'tompohl', 'Tom Pohl',
                       'https://pbs.twimg.com/profile_images/378800000102859706'
                       '/83b823ec53247f689a48d5d3bdeeeb16_normal.jpeg',
                       'Des Moines, Iowa', 'http://t.co/NdcgVZ9Un6',
                       'http://t.co/FN9hFrj9Mm', 0, 681, 661), (
                       1215702054.0, 1449070777.562126, 'jtrajewski',
                       'Jonathan Rajewski',
                       'https://pbs.twimg.com/profile_images/659825753'
                       '/Rajewski_Pic_normal.jpg',
                       'Burlington, Vermont',
                       'Director of @SenatorLeahy Center for Digital '
                       'Investigation, @Champlainedu Professor, Forensic '
                       'Examiner - Vermont ICAC, Marathoner, Bonsai enthusiast',
                       'http://t.co/GqYJCMnCeq', 0, 1165, 411), (
                       1228137407.0, 1449070777.561792, 'PacktPub',
                       'Packt Publishing',
                       'https://pbs.twimg.com/profile_images/629601062660517888'
                       '/B7htKTzE_normal.png',
                       'Birmingham, UK',
                       'Providing books, eBooks, video tutorials, and articles '
                       'for IT developers, administrators, and users.',
                       'http://t.co/vEPCgOu235', 0, 10285, 3589), (
                       1228558254.0, 1449070590.976144, 'taylorswift13',
                       'Taylor Swift',
                       'https://pbs.twimg.com/profile_images/505200807503867904'
                       '/osJXmYRl_normal.jpeg',
                       '', 'Born in 1989.', 'http://t.co/KqIvCWX3nG', 0,
                       66799210,
                       245), (1235576198.0, 1449070777.5616121, 'SANSInstitute',
                              'SANS Institute',
                              'https://pbs.twimg.com/profile_images/591241253574070274/d8f5Oa1o_normal.png',
                              'Worldwide',
                              'SANS is the most trusted and by far the largest '
                              'source for computer security, IT and '
                              'information '
                              'security training, certification and research '
                              'in '
                              'the world.',
                              'http://t.co/AJ81JwpA9v', 0, 67147, 330), (
                       1235845109.0, 1449070777.562701, 'sansforensics',
                       'SANS DFIR',
                       'https://pbs.twimg.com/profile_images/378800000054415512'
                       '/bc6f1e94c6d2fb92de60876c3d7b911c_normal.jpeg',
                       '',
                       "The world's leading Digital Forensics and Incident "
                       "Response provider.   This feed updates you on latest "
                       "DFIR news, events, and training.",
                       'http://t.co/wYvSrf8KQj', 1, 34170, 53), (
                       1236442370.0, 1449070463.640963, 'RihannaDaily',
                       'RihannaDaily.com',
                       'https://pbs.twimg.com/profile_images/664820263507386368'
                       '/iXq_o4XC_normal.png',
                       'Poland/Brazil',
                       "The number 1 and official Rihanna source since 2005. "
                       "Rihanna's 8th studio album ANTI coming soon. Run by "
                       "Natalie & Rodrigo.",
                       'https://t.co/7hD0Py5x9x', 0, 554491, 3786), (
                       1238981366.0, 1449070763.890156, 'danpoolio',
                       'Daniel Poole',
                       'https://pbs.twimg.com/profile_images/1684044583'
                       '/image_normal.jpg',
                       '',
                       'Scratch golfer (I wish that were true), Dave Matthews '
                       'loyalist, trying to enjoy everything this world gives!',
                       None, 0, 256, 1436), (
                       1240818221.0, 1449070463.641476, 'xchatty',
                       'Simson Garfinkel',
                       'https://pbs.twimg.com/profile_images/316695550'
                       '/simson_normal.png',
                       'Washington DC', 'I have a red shirt and sandals.', None,
                       0, 267, 88), (
                       1254519453.0, 1449070463.641043, 'rihanna', 'Rihanna',
                       'https://pbs.twimg.com/profile_images/582747937958076418'
                       '/ZrNhtrD2_normal.jpg',
                       'ANTI',
                       'Excited to share this with you!! #ANTIdiaRy — '
                       'https://t.co/hlEU70f83R',
                       'https://t.co/hlEU70f83R', 0, 53108052, 1149), (
                       1269366066.0, 1449070777.561471, 'Cellebrite_UFED',
                       'Cellebrite Forensics',
                       'https://pbs.twimg.com/profile_images/569823929619857408'
                       '/8X3wetwW_normal.jpeg',
                       '',
                       'Helping government, corporate and private '
                       'investigators '
                       'worldwide to extract, decode and analyze mobile device '
                       'data in a forensically sound and legal manner.',
                       'http://t.co/GwCmMYy2QF', 1, 4588, 2133), (
                       1279141276.0, 1449070698.298584, 'CutonDime25',
                       'Lesean McCoy',
                       'https://pbs.twimg.com/profile_images/585797049968435201'
                       '/WBEutaXs_normal.jpg',
                       'Philadelphia - Harrisburg Pa',
                       'Running Back of the Buffalo Bills Proud Pitt AlumThe '
                       'next best thing',
                       'http://t.co/ihuTmtYbtX', 0, 491970, 126), (
                       1317324887.0, 1449070777.562577, 'Android', 'Android',
                       'https://pbs.twimg.com/profile_images/616076655547682816'
                       '/6gMRtQyY_normal.jpg',
                       'Mountain View, CA',
                       'News, tips, and tricks direct from the Android team.',
                       'http://t.co/WHg9n3cypK', 0, 8471696, 51), (
                       1318947363.0, 1449070763.890719, 'Fitmotiva4u',
                       'Fitness Motivation',
                       'https://pbs.twimg.com/profile_images/665628868183777282'
                       '/ULbAyTEm_normal.png',
                       '',
                       'Stay motivated with your weight loss plan or workout '
                       'routine with these 24 popular quotes and sayings.',
                       'https://t.co/s7PgzmQDYL', 0, 63383, 52567), (
                       1327610054.0, 1449070781.800142, 'HeatherMahalik',
                       'Heather Mahalik',
                       'https://pbs.twimg.com/profile_images/643933136162689024'
                       '/g7dFxGlX_normal.jpg',
                       'Pennsylvania, USA',
                       'Digital Forensics Professional, SANS Senior '
                       'Instructor, '
                       'wife, mama, author, serial vacationer, horse lover and '
                       'simply over-scheduled!',
                       'http://t.co/PKqs8sNY4T', 1, 2699, 421), (
                       1364400451.0, 1449070763.890461, 'EcycleLtd',
                       'Ecycle Ltd',
                       'https://pbs.twimg.com/profile_images/419935576356581376'
                       '/KcVx4_Ck_normal.jpeg',
                       'Tonypandy, South Wales',
                       'ICT Asset Management Specialists',
                       'http://t.co/HCvRnp058x', 0, 342, 801), (
                       1386820071.0, 1449070463.64162, '_Xxinfinity',
                       'K-money ©larke',
                       'https://pbs.twimg.com/profile_images/666460874715111424'
                       '/HpJoVjIb_normal.jpg',
                       '', ':)', None, 0, 271, 208), (
                       1419894260.0, 1449070463.641548, 'twodoorsdownbar',
                       'Two Doors Down',
                       'https://pbs.twimg.com/profile_images/577990010378420224'
                       '/_X6-HWMM_normal.png',
                       '',
                       'Starting out as a labor of love, Two Doors Down is our '
                       'dream come true.',
                       'http://t.co/GtEWFDwQvl', 0, 13, 19), (
                       1427599060.0, 1449070605.318477, 'taylorlandia13',
                       'Taylorlandia',
                       'https://pbs.twimg.com/profile_images/593937270664732672'
                       '/5xENqWVs_normal.jpg',
                       '', 'Welcome to TAYLORLANDIA', 'https://t.co/Jt4vV6f6FC',
                       0, 7876, 5975), (
                       1428561531.0, 1449070777.56089, 'AppleWatchGuru',
                       'AppleWatchGuru',
                       'https://pbs.twimg.com/profile_images/586057290303799297'
                       '/MFoKYas8_normal.jpg',
                       'London, England', 'All and everything \uf8ffWatch',
                       'http://t.co/3VjGvnnoJy', 0, 4829, 4013), (
                       1428960132.0, 1449070777.5611591, 'pickyourdental',
                       'PickYourDentalPlan',
                       'https://pbs.twimg.com/profile_images/587728170402459648'
                       '/c3MSzS1D_normal.png',
                       'Nationwide',
                       'We make it easy to find the dental plan that works for '
                       'you. Compare a wide array of plans to meet your needs '
                       'and budget.',
                       'http://t.co/BZA2KfE5GL', 0, 191, 340), (
                       1449070208.0, 1449070698.298762, 'rosegoldgrl',
                       'Rose Gold',
                       'https://pbs.twimg.com/profile_images/672075764372774912'
                       '/hOhNiHtK_normal.jpg',
                       '', '', None, 0, 2, 106), (
                       1449070462.0, 1449070778.648741, 'hankfresh1',
                       'Hank fresh',
                       'https://pbs.twimg.com/profile_images/672076572120236032'
                       '/C8VL4fvH_normal.jpg',
                       '', '', None, 0, 3, 121)]

    self.assertIsNone(result.error_message)
    self.assertFalse(result.has_error)
    self.assertEqual(expected_data, result.data)

  def testExecuteQueryWithJoin(self):
    """test the execution of a more complex query"""
    query = ('SELECT Statuses.date AS date, Statuses.text AS text,'
             ' Statuses.userId AS user_id, Users.name AS name, '
             'Statuses.retweetCount AS '
             'retweetCount, Statuses.favoriteCount AS favoriteCount, '
             'Statuses.favorited AS favorited, Statuses.updatedAt AS updatedAt '
             'FROM Statuses LEFT join Users ON Statuses.userId = Users.id '
             'ORDER BY date')
    result = self.execute.executeQuery(query)
    expected_data = [(1410435976.0, 'Never forget. http://t.co/L7bjWue1A2',
                      475222380, 'Heather Mahalik', 2, 3, 0,
                      1449070777.1575031), (1447685941.0,
                                            "We don't care how you spend your "
                                            "$5 voucher - we just want to "
                                            "hear from you "
                                            "https://t.co/f4aNishzqk "
                                            "https://t.co/VtVaTY4Lh4",
                                            17778401, 'Packt Publishing', 0, 0,
                                            0, 1449070777.569438), (
                       1447686458.0,
                       'Buy Practical Mobile Forensics! '
                       'https://t.co/ODVj85RJbz',
                       475222380, 'Heather Mahalik', 0, 0, 0,
                       1449070777.569268),
                     (1447688764.0,
                      '#FOR408 is headed to #Philly in February. Let '
                      '@HeatherMahalik show you how to master '
                      '#WindowsForensics https://t.co/khrRBkUKEu',
                      22280436, 'SANS DFIR', 1, 1, 0, 1449070777.570498), (
                       1447688796.0,
                       'RT @sansforensics: #FOR408 is headed to #Philly in '
                       'February. Let @HeatherMahalik show you how to master '
                       '#WindowsForensics https://t.co/khrR…',
                       475222380, 'Heather Mahalik', 1, 0, 0,
                       1449070777.569604),
                     (1447704172.0,
                      'Call for papers is now open for #DFIRSummit 2016. '
                      'Submit by Dec18. More info here: '
                      'https://t.co/W4Ks4ylebI  #DFIR https://t.co/821YSYwClM',
                      22280436, 'SANS DFIR', 13, 6, 0, 1449070777.569118), (
                       1447766405.0,
                       'Exclusive offer! #Cellebrite contributes 30 FREE iOS '
                       '8.x unlocks to the forensic community: '
                       'https://t.co/k0mzHp8h5n https://t.co/IlwrTCp7ww',
                       125728081, 'Cellebrite Forensics', 7, 6, 0,
                       1449070777.573579), (1447766806.0,
                                            'RT @Cellebrite_UFED: Exclusive '
                                            'offer! #Cellebrite contributes 30 '
                                            'FREE iOS 8.x unlocks to the '
                                            'forensic community: '
                                            'https://t.co/k0mzHp8h5n ht…',
                                            475222380, 'Heather Mahalik', 7, 0,
                                            0,
                                            1449070777.573422), (1447766816.0,
                                                                 'RT '
                                                                 '@sansforensics: Call for papers is now open for #DFIRSummit 2016. Submit by Dec18. More info here: https://t.co/W4Ks4ylebI  #DFIR https:…',
                                                                 475222380,
                                                                 'Heather '
                                                                 'Mahalik',
                                                                 13, 0, 0,
                                                                 1449070777.568928),
                     (1447846192.0,
                      'If you are interested in OSX forensics, all of '
                      '@iamevltwin presentations are pure gold! '
                      'https://t.co/GtOg76Qbr3',
                      14388264, 'Tom Pohl', 7, 11, 0, 1449070777.568352), (
                       1447856756.0,
                       'Well done, @ElcomSoft https://t.co/wNQ54OQvne '
                       '#iPhonePhysical #FOR585',
                       475222380, 'Heather Mahalik', 0, 0, 0,
                       1449070777.564301),
                     (1447856772.0,
                      'RT @tompohl: If you are interested in OSX forensics, '
                      'all of @iamevltwin presentations are pure gold! '
                      'https://t.co/GtOg76Qbr3',
                      475222380, 'Heather Mahalik', 7, 0, 0,
                      1449070777.5678701), (1447862914.0,
                                            'When is a smartphone the best '
                                            'evidence? Seems to be in the '
                                            '#ParisAttacks Be prepared to '
                                            'find evidence! #FOR585 '
                                            'https://t.co/dp4tprKaZH',
                                            475222380, 'Heather Mahalik', 0, 0,
                                            0, 1449070777.57437), (1447862960.0,
                                                                   '@SwiftOnSecurity Try this https://t.co/z27rhlCvFO',
                                                                   475222380,
                                                                   'Heather '
                                                                   'Mahalik',
                                                                   0, 0, 0,
                                                                   1449070777.57649),
                     (1447862970.0,
                      '@4ensfresh @SwiftOnSecurity @ElcomSoft '
                      'https://t.co/z27rhlCvFO',
                      475222380, 'Heather Mahalik', 0, 0, 0, 1449070777.564983),
                     (1447864315.0,
                      'Official Magnetic Charging Dock for Apple Watch '
                      'launches for $79 https://t.co/MDK17Zu9rV '
                      'https://t.co/uU1xipsUkB',
                      3150614614, 'AppleWatchGuru', 14, 22, 0,
                      1449070777.573126), (1447865009.0,
                                           'RT @AppleWatchGuru: Official '
                                           'Magnetic Charging Dock for Apple '
                                           'Watch launches for $79 '
                                           'https://t.co/MDK17Zu9rV '
                                           'https://t.co/uU1xipsUkB',
                                           475222380, 'Heather Mahalik', 14, 0,
                                           0, 1449070777.5727859), (
                       1447865110.0,
                       'Two weeks until #FOR408 vLive kicks off. '
                       '#WindowsForensics https://t.co/5MZmKtDg6n #PJsWelcome '
                       '#RelaxLearnLaugh',
                       475222380, 'Heather Mahalik', 1, 2, 0,
                       1449070777.570037),
                     (1447886537.0,
                      'Master Windows Forensics w/ @HeatherMahalik | Newly '
                      'updated FOR408 starts Dec. 1 via vLive: '
                      'https://t.co/PXQRMxsZaq https://t.co/8yuexroRhT',
                      21877065, 'SANS Institute', 16, 7, 0, 1449070777.5754309),
                     (1447888301.0,
                      'RT @SANSInstitute: Master Windows Forensics w/ '
                      '@HeatherMahalik | Newly updated FOR408 starts Dec. 1 '
                      'via vLive: https://t.co/PXQRMxsZaq http…',
                      475222380, 'Heather Mahalik', 16, 0, 0,
                      1449070777.575239), (1447964533.0,
                                           'If anyone is interested in '
                                           'jumping to academia to teach '
                                           '#dfir send me a message. We may '
                                           'have an opportunity for a '
                                           'full-time position.',
                                           15378399, 'Jonathan Rajewski', 14, 1,
                                           0, 1449070777.574604), (1447966303.0,
                                                                   'RT '
                                                                   '@jtrajewski: If anyone is interested in jumping to academia to teach #dfir send me a message. We may have an opportunity for a full-time…',
                                                                   475222380,
                                                                   'Heather '
                                                                   'Mahalik',
                                                                   14, 0, 0,
                                                                   1449070777.574502),
                     (1448024497.0,
                      'Come talk #StageFright and #XcodeGhost #mobilemalware '
                      'with @HeatherMahalik Dec7 - Take #FOR585 in '
                      '#Chantilly, #VA https://t.co/Hf2DJJLiAc',
                      22280436, 'SANS DFIR', 2, 1, 0, 1449070777.564809), (
                       1448026018.0,
                       'RT @sansforensics: Come talk #StageFright and '
                       '#XcodeGhost #mobilemalware with @HeatherMahalik Dec7 - '
                       'Take #FOR585 in #Chantilly, #VA https:…',
                       475222380, 'Heather Mahalik', 2, 0, 0,
                       1449070777.564648),
                     (1448038448.0,
                      "Thanksgiving lunch at Jack's school. #thankful "
                      "https://t.co/OeHyOIOqnp",
                      475222380, 'Heather Mahalik', 0, 1, 0, 1449070777.57017),
                     (1448289925.0,
                      'Just a few seats left! Treat yourself to updated '
                      '#FOR585 material before the holidays hit. '
                      'https://t.co/rjItNWt91G Chantilly, VA.',
                      475222380, 'Heather Mahalik', 1, 2, 0, 1449070777.569891),
                     (1448301676.0,
                      '@Peej_Jones Of course! New labs, more malware, '
                      'Apple Watch!',
                      475222380, 'Heather Mahalik', 0, 0, 0, 1449070777.572495),
                     (1448364719.0,
                      '"Smartphone tech is new and data formats are '
                      'unfamiliar to many" - #FOR585 attendee '
                      'https://t.co/TxNCRFiWlz',
                      22280436, 'SANS DFIR', 2, 6, 0, 1449070777.575851), (
                       1448383874.0,
                       "Don't miss keynote #ConvergenceForensics &amp; #FOR408 "
                       "with @HeatherMahalik @ #SANSPhilly - Feb 29 - Mar 5 "
                       "https://t.co/XSg7kOcdS1",
                       22280436, 'SANS DFIR', 1, 2, 0, 1449070777.565448), (
                       1448387038.0,
                       "RT @sansforensics: Don't miss keynote "
                       "#ConvergenceForensics &amp; #FOR408 with "
                       "@HeatherMahalik @ #SANSPhilly - Feb 29 - Mar 5 "
                       "https://t.co/XSg7…",
                       475222380, 'Heather Mahalik', 1, 0, 0,
                       1449070777.565608),
                     (1448387060.0,
                      'RT @sansforensics: "Smartphone tech is new and data '
                      'formats are unfamiliar to many" - #FOR585 attendee '
                      'https://t.co/TxNCRFiWlz',
                      475222380, 'Heather Mahalik', 2, 0, 0, 1449070777.575728),
                     (1448400791.0,
                      "I've had it with this day... I need a drink. :/",
                      475222380, 'Heather Mahalik', 0, 3, 0, 1449070777.572604),
                     (1448405339.0, '@nerdiosity https://t.co/BBRczm6q2K',
                      475222380, 'Heather Mahalik', 0, 0, 0, 1449070777.570684),
                     (1448405349.0, '@_devonkerr_ you too!', 475222380,
                      'Heather Mahalik', 0, 0, 0, 1449070777.5760021), (
                       1448456433.0,
                       'Follow us and learn how we can help you save $$ on '
                       'your dental care.',
                       3153652970, 'PickYourDentalPlan', 0, 3, 0,
                       1449070777.563392), (
                       1448462074.0, '@DAVNADS amazing.', 475222380,
                       'Heather Mahalik', 0, 1, 0, 1449070777.56871), (
                       1448465899.0,
                       'It is time. #ChooseYourSide https://t.co/3hC2xVtChI '
                       'https://t.co/g167D0IQnn',
                       382267114, 'Android', 285, 623, 0, 1449070777.566802), (
                       1448467293.0,
                       'Look out @normsbeerwine and @viennavitner I am coming '
                       'back to VA to buy everything in stock.',
                       475222380, 'Heather Mahalik', 0, 1, 0,
                       1449070777.563908),
                     (1448467337.0,
                      'Have to get this into #FOR585 https://t.co/Ekw7Y0gwFE',
                      475222380, 'Heather Mahalik', 0, 1, 0, 1449070777.566287),
                     (1448468327.0,
                      "@brianjmoran Sweet! How did you collect the data? I'm "
                      "too impatient to wait on the blog.",
                      475222380, 'Heather Mahalik', 0, 0, 0, 1449070777.567249),
                     (1448468636.0,
                      "@brianjmoran It's going to be a great blog. Can't wait "
                      "to see it.",
                      475222380, 'Heather Mahalik', 0, 1, 0, 1449070777.573247),
                     (1448469892.0,
                      "Forensics on the #PRIV Let's do this @BryanOnSecurity "
                      "#blackberry #android #FOR585",
                      475222380, 'Heather Mahalik', 0, 0, 0, 1449070777.562979),
                     (1448469949.0, '@brianjmoran Food for thought...',
                      475222380, 'Heather Mahalik', 0, 0, 0, 1449070777.566136),
                     (1448470015.0,
                      '@packtauthors @PacktPub Can one of you email me about '
                      'ordering more books? heather@smarterforensics.com',
                      475222380, 'Heather Mahalik', 0, 0, 0,
                      1449070777.5722651), (1448579796.0,
                                            'Happy Thanksgiving! Hope you are '
                                            'enjoying your day and counting '
                                            'not your blessings. :)',
                                            475222380, 'Heather Mahalik', 0, 1,
                                            0, 1449070777.572378), (
                       1448640002.0,
                       'Potty training all weekend. Pray for my sanity!',
                       475222380, 'Heather Mahalik', 0, 1, 0,
                       1449070777.567062),
                     (1448897682.0,
                      'Today I celebrate @domenicacrognal Happy birthday!!!!',
                      475222380, 'Heather Mahalik', 0, 0, 0, 1449070777.575577),
                     (1448904126.0,
                      'Well done @facebook Glad to see companies supporting '
                      'parental/maternity leave!',
                      475222380, 'Heather Mahalik', 0, 0, 0, 1449070777.56403),
                     (1448919966.0,
                      'Thinking about #vLive courses? Only two more days to '
                      'register #FOR408 with @heathermahalik &amp; get $750 '
                      'off. https://t.co/Hf2DJJLiAc',
                      22280436, 'SANS DFIR', 1, 1, 0, 1449070777.5742269), (
                       1448920159.0,
                       'RT @sansforensics: Thinking about #vLive courses? '
                       'Only two more days to register #FOR408 with '
                       '@heathermahalik &amp; get $750 off. https://t.co/…',
                       475222380, 'Heather Mahalik', 1, 0, 0, 1449070777.57136),
                     (
                       1448973945.0,
                       'Still time to register #FOR572 with @philhagen @ '
                       '#SANSCDI to incorporate #networkforensics into your '
                       'investigations https://t.co/NE9FJAtbYJ',
                       22280436, 'SANS DFIR', 3, 2, 0, 1449070777.57387), (
                       1448976072.0,
                       'Rihanna on @Spotify in 2015: 1 billion streams and 57 '
                       'million listeners. https://t.co/Q6y3MmTIgO',
                       23205844, 'RihannaDaily.com', 1076, 1434, 0,
                       1449070463.645055), (1448983988.0,
                                            '#FOR408 vLive kicks off tonight. '
                                            'Better get ready for some '
                                            'Holiday cheer up in here. :)',
                                            475222380, 'Heather Mahalik', 1, 2,
                                            0,
                                            1449070777.56599), (1448984000.0,
                                                                'RT '
                                                                '@sansforensics: Still time to register #FOR572 with @philhagen @ #SANSCDI to incorporate #networkforensics into your investigations http…',
                                                                475222380,
                                                                'Heather '
                                                                'Mahalik',
                                                                3, 0, 0,
                                                                1449070777.565143),
                     (1448984034.0,
                      '@JZdziarski I really push it by writing Merry '
                      'Christmas on our "Holiday" Cards...',
                      475222380, 'Heather Mahalik', 0, 0, 0, 1449070777.566946),
                     (1449002890.0,
                      "Didn't win Week 12? New week, fresh start! Who are you "
                      "taking on your team? JOIN NOW: https://t.co/MJn9OyI5rB",
                      166718532, 'Lesean McCoy', 1, 10, 0, 1449070698.299211), (
                       1449013753.0,
                       '#FOR408 kicking off in 10 mins. #vLive Let the fun '
                       'begin! https://t.co/nXVs862vVn',
                       475222380, 'Heather Mahalik', 1, 4, 0, 1449070777.57034),
                     (
                       1449035373.0,
                       'Most streamed female artist of 2015! '
                       'https://t.co/kXKeuBb3Rx',
                       79293791, 'Rihanna', 5508, 9669, 0, 1449070463.648808), (
                       1449057562.0,
                       'David Cameron says he respects those who oppose air '
                       'strikes as #SyriaVote debate begins '
                       'https://t.co/1tHa9YJF3M https://t.co/9PBop9ZiSi',
                       5402612, 'BBC Breaking News', 358, 324, 0,
                       1449070544.3342), (1449060344.0,
                                          'Bring your #mobileforensics poster '
                                          'to #SANSMcLean &amp; use it while '
                                          'taking #FOR585 on Feb15 '
                                          'https://t.co/vxiMXNqm56 '
                                          'https://t.co/7jROD60dje',
                                          22280436, 'SANS DFIR', 10, 6, 0,
                                          1449070777.572115), (1449061336.0,
                                                               'Making '
                                                               'friends on '
                                                               'Hamilton '
                                                               'Island. '
                                                               'https://t.co/26SLoiCUZt',
                                                               17919972,
                                                               'Taylor Swift',
                                                               11453, 39496, 1,
                                                               1449070590.9766111),
                     (1449065972.0,
                      'RT @sansforensics: Bring your #mobileforensics poster '
                      'to #SANSMcLean &amp; use it while taking #FOR585 on '
                      'Feb15 https://t.co/vxiMXNqm56 https:/…',
                      475222380, 'Heather Mahalik', 10, 0, 0,
                      1449070777.571907), (
                       1449070368.0, 'My first tweet!', 4351838729, 'Rose Gold',
                       0, 1, 1, 1449070698.2989101), (1449070373.0,
                                                      "RT @CutonDime25: "
                                                      "Didn't win Week 12? "
                                                      "New week, fresh start! "
                                                      "Who are you taking on "
                                                      "your team? JOIN NOW: "
                                                      "https://t.co/MJn9OyI5rB",
                                                      4351838729, 'Rose Gold',
                                                      1,
                                                      0, 0, 1449070698.299088),
                     (
                       1449070543.0,
                       'RT @taylorswift13: Making friends on Hamilton Island. '
                       'https://t.co/26SLoiCUZt',
                       4351934314, 'Hank fresh', 11453, 0, 1,
                       1449070590.976365),
                     (1449070737.0, '@rosegoldgrl hi', 4351934314, 'Hank fresh',
                      0, 0, 0, 1449070738.070436), (
                       1449070761.0, 'Missing Florida https://t.co/yCabNeBaOx',
                       4351934314, 'Hank fresh', 0, 0, 0, 1449070761.790525)]

    self.assertIsNone(result.error_message)
    self.assertFalse(result.has_error)
    self.assertEqual(expected_data, result.data)


if __name__ == '__main__':
  unittest.main()
