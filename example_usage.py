from client import TreeStructuredSyntheticCurriculumSynthesizerClient

def main():
    client = TreeStructuredSyntheticCurriculumSynthesizerClient()
    res = client.synthesize_pedagogical_curriculum('Distributed Systems Consensus & Paxos Proofs', 20)
    print('Synthetic Curriculum: ' + res['curriculum_job_id'] + ' | ' + res['domain'])
    print('Chapters: ' + str(res['textbook_chapters_generated']) + ' | Depth: ' + str(res['pedagogical_depth_score_pct']) + '%')
    print('Socratic Exercises: ' + str(res['socratic_verification_exercises_count']))
    print('Dataset URL: ' + res['synthetic_dataset_jsonl_url'])

if __name__ == '__main__':
    main()
